import streamlit as st
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database Configuration
DATABASE_URL = "postgresql://postgres:root@localhost:5432/banking"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

# User Model
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    balance = Column(Float, default=0.0)

# Initialize Database
def init_db():
    Base.metadata.create_all(engine)

# Streamlit App
st.title("Simple Banking System")
init_db()

# Session State for User Authentication
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.user_id = None

# Signup Function
def signup():
    st.subheader("Signup")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Register"):
        session = SessionLocal()
        if session.query(User).filter_by(username=username).first():
            st.error("Username already exists!")
        else:
            new_user = User(username=username, password=password, balance=0.0)
            session.add(new_user)
            session.commit()
            st.success("Signup successful! Please login.")
        session.close()

# Login Function
def login():
    st.subheader("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        session = SessionLocal()
        user = session.query(User).filter_by(username=username, password=password).first()
        if user:
            st.session_state.logged_in = True
            st.session_state.user_id = user.id
            st.success("Login successful!")
            st.rerun()
        else:
            st.error("Invalid username or password.")
        session.close()

# Banking Functions
def banking():
    session = SessionLocal()
    user = session.query(User).filter_by(id=st.session_state.user_id).first()
    st.subheader(f"Welcome, {user.username}")
    st.write(f"Your Current Balance: ₹{user.balance}")
    
    amount = st.number_input("Enter Amount", min_value=0.0, step=0.01)
    if st.button("Deposit"):
        user.balance += amount
        session.commit()
        st.success(f"Deposited ₹{amount}")
        st.rerun()
    
    if st.button("Withdraw"):
        if user.balance >= amount:
            user.balance -= amount
            session.commit()
            st.success(f"Withdrawn ₹{amount}")
            st.rerun()
        else:
            st.error("Insufficient balance!")
    session.close()

# Navigation
if not st.session_state.logged_in:
    option = st.sidebar.radio("Choose an option", ["Login", "Signup"])
    if option == "Login":
        login()
    else:
        signup()
else:
    banking()
    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.user_id = None
        st.rerun()
