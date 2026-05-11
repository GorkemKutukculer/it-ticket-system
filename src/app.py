import streamlit as st
from ticket_manager import TicketManager
import pandas as pd

st.set_page_config(page_title="IT Helpdesk Yönetim", page_icon="🖥️", layout="wide")

manager = TicketManager()
db_users = manager.get_all_users()

if db_users:
    user_dict = {row[0]: row[1] for row in db_users}
else:
    user_dict = {1: "Kullanıcı Bulunamadı"}

st.title("🖥️ IT Helpdesk Yönetim Paneli")
st.markdown("**Marmara Üniversitesi Bilgi İşlem Destek Sistemi**")
st.markdown("---")

st.sidebar.header("🛠️ Hızlı İşlemler")

with st.sidebar.expander("➕ Yeni Destek Talebi Aç", expanded=False):
    with st.form("ticket_form"):
        user_id = st.selectbox("Talebi Açan", 
                               options=list(user_dict.keys()), 
                               format_func=lambda x: user_dict[x])
        
        title = st.text_input("Sorun Başlığı")
        description = st.text_area("Açıklama")
        priority = st.selectbox("Öncelik", ["Low", "Medium", "High", "Critical"])
        submit = st.form_submit_button("Talebi Oluştur")

        if submit:
            if title and description:
                manager.create_ticket(title, description, priority, user_id)
                st.success("Talep oluşturuldu!")
                st.rerun()

st.sidebar.markdown("---")
st.sidebar.subheader("✅ Talebi Tamamla")
ticket_id_to_update = st.sidebar.number_input("Kapatılacak Bilet ID", min_value=1, step=1)

st.sidebar.markdown("---")
st.sidebar.subheader("🗑️ Talebi Sil")
ticket_id_to_delete = st.sidebar.number_input("Silinecek Bilet ID", min_value=1, step=1, key="delete_id")

if st.sidebar.button("Kalıcı Olarak Sil"):
    manager.delete_ticket(ticket_id_to_delete)
    st.sidebar.success(f"ID {ticket_id_to_delete} başarıyla silindi!")
    st.rerun()

if st.sidebar.button("Çözüldü Olarak İşaretle"):
    manager.update_ticket_status(ticket_id_to_update, 'Resolved')
    st.sidebar.success(f"ID {ticket_id_to_update} başarıyla kapatıldı!")
    st.rerun()

tickets = manager.get_all_tickets()

if tickets:
    df = pd.DataFrame([list(row) for row in tickets], 
                      columns=["ID", "Başlık", "Açıklama", "Öncelik", "Durum", "Açan Kişi"])
    
    col1, col2, col3 = st.columns(3)
    
    toplam_talep = len(df)
    acik_talep = len(df[df["Durum"] == "Open"])
    cozulen_talep = len(df[df["Durum"] == "Resolved"])
    
    col1.metric(label="📌 Toplam Talep", value=toplam_talep)
    col2.metric(label="🔥 Açık Talepler", value=acik_talep, delta=f"-{cozulen_talep} Çözülen", delta_color="inverse")
    
    cozulme_orani = int((cozulen_talep / toplam_talep) * 100) if toplam_talep > 0 else 0
    col3.metric(label="🚀 Çözülme Oranı", value=f"%{cozulme_orani}")

    st.markdown("<br>", unsafe_allow_html=True)

    def color_status(val):
        color = '#ff4b4b' if val == 'Open' else '#21c354'
        return f'color: {color}; font-weight: bold'

    tab1, tab2 = st.tabs(["📋 Tüm Talepler Listesi", "🔍 Çalışana Göre Filtrele"])

    with tab1:
        st.dataframe(df.style.applymap(color_status, subset=['Durum']), use_container_width=True)

    with tab2:
        calisanlar = ["Hepsi"] + list(user_dict.values())
        secilen_kisi = st.selectbox("Lütfen biletlerini görmek istediğiniz çalışanı seçin:", calisanlar)
        
        if secilen_kisi != "Hepsi":
            filtered_df = df[df["Açan Kişi"] == secilen_kisi]
        else:
            filtered_df = df
            
        if not filtered_df.empty:
            st.dataframe(filtered_df.style.applymap(color_status, subset=['Durum']), use_container_width=True)
        else:
            st.warning(f"{secilen_kisi} adına henüz bir talep açılmamış.")

else:
    st.info("Sistemde henüz kayıtlı destek talebi bulunmuyor.")