import streamlit as st


st.set_page_config(
  page_title="Magellan",
  page_icon="./images/monsterball.png"
)
st.title("Magellan lalalal")
st.markdown('**포켓못** 사진을 **추가** 해보등가....')

type_emoji_dict = {
    "노말": "⚪",
    "격투": "✊",
    "비행": "🕊",
    "독": "☠️",
    "땅": "🌋",
    "바위": "🪨",
    "벌레": "🐛",
    "고스트": "👻",
    "강철": "🤖",
    "불꽃": "🔥",
    "물": "💧",
    "풀": "🍃",
    "전기": "⚡",
    "에스퍼": "🔮",
    "얼음": "❄️",
    "드래곤": "🐲",
    "악": "😈",
    "페어리": "🧚"
}

pokemon = {
  "name" : "누오",
  "types" : ["물", "땅"],
  "image_url" : "https://i.namu.wiki/i/W2JS6BjC2ET8_laTnzCMvReYmIgRPGSsmbSl1ZAQmjWE1e1hBJ9TuiHtUOny7acsb2Qqz3shnukm0frKhsgCBXuZcJYCnGVwWgxR22GXU2tEg9vww_Ud7uvqr13GKOlLMxMfkml9ut4JGQD16_wzCw.webp"
}

with st.expander(label=pokemon["name"], expanded=True):
  st.image(pokemon["image_url"])
  emoji_types = [f"{type_emoji_dict[x]} {x}" for x in pokemon["types"]]
  st.subheader(" / ".join(emoji_types))
