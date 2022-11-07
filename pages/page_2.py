import datetime
import streamlit as st

with st.form(key='profile'):
    #テキストボックス
        name=st.text_input('名前')
        address=st.text_input('住所')

        #セレクトボタン
        #ラジオボタン
        #age_category=st.selectbox(
        age_category=st.radio(
            '年齢層',
            ('子供（１８歳未満）','大人（１８歳以上）'))

        #複数選択
        hobby=st.multiselect(
            '趣味',
            ('スポーツ','読書','プログラミング','アニメ')
        )
        #チェックボックス
        mail_subscribe=st.checkbox('メールマガジンを購読する')
        if mail_subscribe:
            message=' はい'
        else:
            message=' いいえ'

        #スライダー
        height=st.slider('身長',min_value=110,max_value=210)
        #日付
        start_date=st.date_input(
            '開始日',
            datetime.date(2022,7,1))

        #カラーピッカー
        color=st.color_picker('テーマカラー','#00f900')
        
        #ボタン
        submit_btn=st.form_submit_button('送信')
        cancel_btn=st.form_submit_button('キャンセル')
        if submit_btn:
            st.text(f'ようこそ!{name}さん！{address}に書簡を送りました！')
            st.text(f'年齢層:{age_category}')
            st.text(f'趣味:{", ".join(hobby)}')
            st.text(f'メルマガ:{message}')
