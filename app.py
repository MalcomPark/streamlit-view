import streamlit as st
print("page reload")
st.set_page_config(
  page_title="Pokemon",
  page_icon="./images/monsterball.png"
)
st.markdown("""
<style>
            h1{
                color: grey;
                }
            img {
                max-height:300px
                }
            .streamlit-expanderContent div {
                display: flex;
                justify-content: center;
                font-size: 20px;
            }
            </style>
""", unsafe_allow_html=True)


st.title("Malcom's Picture Database")
st.markdown('Add image with link and name it')

type_emoji_dict = {
    "Normal": "⚪",
    "Fight": "✊",
    "Fly": "🕊",
    "Poison": "☠️",
    "Ground": "🌋",
    "Rock": "🪨",
    "Worm": "🐛",
    "Ghost": "👻",
    "Iron": "🤖",
    "Fire": "🔥",
    "Water": "💧",
    "Grass": "🍃",
    "Electricity": "⚡",
    "Aespa": "🔮",
    "Ice": "❄️",
    "Dragon": "🐲",
    "Evil": "😈",
    "Fairy": "🧚"
}

initial_pokemons = [
    {
        "name": "Pica",
        "types": ["Electricity"],
        "image_url": "https://storage.googleapis.com/firstpenguine-coding-school/pokemons/pikachu.webp"
    },
    {
        "name": "Nuo",
        "types": ["Water", "Ground"],
        "image_url": "https://storage.googleapis.com/firstpenguine-coding-school/pokemons/nuo.webp",
    },
    {
        "name": "Gara",
        "types": ["Water", "Fly"],
        "image_url": "https://storage.googleapis.com/firstpenguine-coding-school/pokemons/garados.webp",
    },
    {
        "name": "Frog",
        "types": ["Water", "Evil"],
        "image_url": "https://storage.googleapis.com/firstpenguine-coding-school/pokemons/frogninja.webp"
    },
    {
        "name": "Luca",
        "types": ["Ice", "Iron"],
        "image_url": "https://storage.googleapis.com/firstpenguine-coding-school/pokemons/lukario.webp"
    },
    {
        "name": "Ace",
        "types": ["Fire"],
        "image_url": "https://storage.googleapis.com/firstpenguine-coding-school/pokemons/acebun.webp"
    },
]

example_pokemon = {
    "name": "Dagda",
    "types": ["Water", "Iron"],
    "image_url": "https://storage.googleapis.com/firstpenguine-coding-school/pokemons/alora_digda.webp"
}

if "pokemons" not in st.session_state:
    st.session_state.pokemons = initial_pokemons

auto_complete=st.toggle("Fill with example")
print("page_reload, auto_complete", auto_complete)
with st.form(key="form"):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input(
            label="Name",
            value=example_pokemon["name"] if auto_complete else ""
            )
    with col2:
        types = st.multiselect(
            label="Character", 
            options=list(type_emoji_dict.keys()),
            max_selections=2,
            default=example_pokemon["types"] if auto_complete else []
            )
    image_url = st.text_input(
        label="image URL",
        value=example_pokemon["image_url"] if auto_complete else "")
    submit = st.form_submit_button(label="ADD")
    if submit:
        if not name:
            st.error("input name")
        elif len(types) == 0:
            st.error("Select at least 1 character")
        else:
            st.success("New Pokemon is added!")
            st.session_state.pokemons.append({
                "name": name,
                "types": types,
                "image_url": image_url if image_url else "./images/default.png"

            })

for i in range(0, len(st.session_state.pokemons), 3):
  row_pokemons = st.session_state.pokemons[i:i+3]
  cols = st.columns(3)
  for j in range(len(row_pokemons)):
      with cols[j]:
          pokemon = row_pokemons[j]
          with st.expander(label=f"**{i+j+1}. {pokemon['name']}**", expanded=True):
              st.image(pokemon["image_url"])
              emoji_types = [f"{type_emoji_dict[x]} {x}" for x in pokemon["types"]]
              st.text(" / ".join(emoji_types))
              delete_button=st.button(label="Remove", key=i+j, use_container_width=True)
              if delete_button:
                  print("delete button clicked")
                  del st.session_state.pokemons[i+j]
                  st.rerun()
