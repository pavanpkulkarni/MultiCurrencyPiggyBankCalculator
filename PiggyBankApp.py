import streamlit as st
from forex_python.converter import CurrencyRates

st.header('Piggy Bank Calculator :pig: :moneybag:')

base_currency = "CAD"
with st.sidebar:

    st.sidebar.image("piggy_bank.png", use_column_width=True)

    base_currency = st.radio('Pick your base currency',['USD','CAD', 'INR'])

    if st.button('Clear All'):
        for key in st.session_state.keys():
            st.session_state[key] = 0
    total_value = 0.0

def get_inr_in_paise(dict_of_inr_coins):
    list_of_coins = []
    weights = []
    weighted_sum = []

    for key, value in dict_of_inr_coins.items():
        list_of_coins.append(value)
        weights.append(int(key[4:]))

    for coins, value in zip(list_of_coins, weights):
        weighted_sum.append(coins * value)

    return sum(weighted_sum)

def get_usd_in_cents(dict_of_usd_coins):
    list_of_coins = []
    weights = []
    weighted_sum = []

    for key, value in dict_of_usd_coins.items():
        list_of_coins.append(value)
        weights.append(int(key[4:]))

    for coins, value in zip(list_of_coins, weights):
        weighted_sum.append(coins * value)

    return sum(weighted_sum)

def get_cad_in_cents(dict_of_cad_coins):
    list_of_coins = []
    weights = []
    weighted_sum = []

    for key, value in dict_of_cad_coins.items():
        list_of_coins.append(value)
        weights.append(int(key[4:]))

    for coins, value in zip(list_of_coins, weights):
        weighted_sum.append(coins * value)

    return sum(weighted_sum)

dict_of_cad_coins = {}
dict_of_usd_coins = {}
dict_of_inr_coins = {}

for key, value in st.session_state.items():
    if(key.startswith("cad")):
        dict_of_cad_coins[key] = value
    if(key.startswith("usd")):
        dict_of_usd_coins[key] = value
    if(key.startswith("inr")):
        dict_of_inr_coins[key] = value

inr = get_inr_in_paise(dict_of_inr_coins)/100
print(f"INR : {inr}")

usd = get_usd_in_cents(dict_of_usd_coins)/100
print(f"USD : {usd}")

cad = get_cad_in_cents(dict_of_cad_coins)/100
print(f"CAD : {cad}")

total_value = 0.0



col1, col2, col3 = st.columns(3)

with col1:
    st.header("CAD :flag-ca:")
    st.number_input("¢1", placeholder="# of coins", step=1, key='cad_001')
    st.number_input("¢5", placeholder="# of coins", step=1, key='cad_005')
    st.number_input("¢10", placeholder="# of coins", step=1, key='cad_010')
    st.number_input("¢25", placeholder="# of coins", step=1, key='cad_025')
    st.number_input("$1", placeholder="# of coins", step=1, key='cad_100')
    st.number_input("$2", placeholder="# of coins", step=1, key='cad_200')
    st.markdown('#')
    st.markdown('#')
    st.markdown('#')
    st.markdown('#')
    st.markdown('#')
    st.markdown('#')
    st.markdown('#')
    st.divider()
    st.text_area("Total (CAD $) :flag-ca: ", value=cad)
    st.divider()

with col2:
    st.header("USD :flag-us:")
    st.number_input("¢1", placeholder="# of coins", step=1, key='usd_001')
    st.number_input("¢5", placeholder="# of coins", step=1, key='usd_005')
    st.number_input("¢10", placeholder="# of coins", step=1, key='usd_010')
    st.number_input("¢25", placeholder="# of coins", step=1, key='usd_025')
    st.number_input("$1", placeholder="# of coins", step=1, key='usd_100')
    st.number_input("$2", placeholder="# of coins", step=1, key='usd_200')
    st.markdown('#')
    st.markdown('#')
    st.markdown('#')
    st.markdown('#')
    st.markdown('#')
    st.markdown('#')
    st.markdown('#')
    st.divider()
    st.text_area("Total (USD $) :flag-us: ", value=usd)
    st.divider()

with col3:
    st.header("INR :flag-in:")
    st.number_input("p1", placeholder="# of coins", step=1, key='inr_001')
    st.number_input("p5", placeholder="# of coins", step=1, key='inr_005')
    st.number_input("p10", placeholder="# of coins", step=1, key='inr_010')
    st.number_input("p25", placeholder="# of coins", step=1, key='inr_025')
    st.number_input("p50", placeholder="# of coins", step=1, key='inr_050')
    st.number_input("₹1", placeholder="# of coins", step=1, key='inr_100')
    st.number_input("₹2", placeholder="# of coins", step=1, key='inr_200')
    st.number_input("₹5", placeholder="# of coins", step=1, key='inr_500')
    st.number_input("₹10", placeholder="# of coins", step=1, key='inr_1000')
    st.divider()
    st.text_area("Total (INR $) :flag-in: ", value=inr)
    st.divider()

#st.write(st.session_state)

#base_currency = st.selectbox('Pick your base currency',['USD','CAD', 'INR'])

c = CurrencyRates()

if(base_currency == "CAD"):
    inr_cad = c.get_rate('INR', 'CAD')
    usd_cad = c.get_rate('USD', 'CAD')
    total_cad = inr_cad*inr + usd_cad*usd + cad
    print(f"Total value in CAD = $ {total_cad}")
    st.sidebar.write(f"Total value in CAD = $ {total_cad}")
elif(base_currency == "INR"):
    cad_inr = c.get_rate('CAD', 'INR')
    usd_inr = c.get_rate('USD', 'INR')
    total_inr = cad_inr*cad + usd_inr*usd + inr
    print(f"Total value in INR = ₹ {total_inr}")
    st.sidebar.write(f"Total value in INR = ₹ {total_inr}")
else:
    inr_usd = c.get_rate('INR', 'USD')
    cad_usd = c.get_rate('CAD', 'USD')
    total_usd = inr_usd*inr + cad_usd*cad + usd
    print(f"Total value in USD = $ {total_usd}")
    st.sidebar.write(f"Total value in USD = $ {total_usd}")
