import hmac
import gspread as gs
import streamlit as st
import numpy


def check_password():
    """Returns `True` if the user had a correct password."""

    def login_form():
        """Form with widgets to collect user information"""
        with st.form("Credentials"):
            st.text_input("Username", key="username")
            st.text_input("Password", type="password", key="password")
            st.form_submit_button("Log in", on_click=password_entered)

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if st.session_state["username"] in st.secrets[
            "passwords"
        ] and hmac.compare_digest(
            st.session_state["password"],
            st.secrets.passwords[st.session_state["username"]],
        ):
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # Don't store the username or password.
            del st.session_state["username"]
        else:
            st.session_state["password_correct"] = False

    # Return True if the username + password is validated.
    if st.session_state.get("password_correct", False):
        return True

    # Show inputs for username + password.
    login_form()
    if "password_correct" in st.session_state:
        st.error("😕 User not known or password incorrect")
    return False


if not check_password():
    st.stop()

# Main Streamlit app starts here
st.set_page_config(page_title="Maintenance Logs", page_icon="🔧", layout="wide")


# ---- Connection to Database ----
credentials = { "type" : st.secrets["gcp_service_account"]["type"],
                "project_id" : st.secrets["gcp_service_account"]["project_id"],
                "private_key_id" : st.secrets["gcp_service_account"]["private_key_id"],
                "private_key" : st.secrets["gcp_service_account"]["private_key"],
                "client_email" : st.secrets["gcp_service_account"]["client_email"],
                "client_id" : st.secrets["gcp_service_account"]["client_id"],
                "auth_uri" : st.secrets["gcp_service_account"]["auth_uri"],
                "token_uri" : st.secrets["gcp_service_account"]["token_uri"],
                "auth_provider_x509_cert_url" : st.secrets["gcp_service_account"]["auth_provider_x509_cert_url"],
                "client_x509_cert_url" : st.secrets["gcp_service_account"]["client_x509_cert_url"],
                "universe_domain" : st.secrets["gcp_service_account"]["universe_domain"],
                }
gc = gs.service_account_from_dict(credentials)
sh = gc.open("Sample-Maintenance-Log")
worksheet = sh.sheet1
data = worksheet.get_all_values()


# ---- Data Table and Edit ----
with st.container():
    st.write("----")
    st.header("Maintenance Logs")
    st.write("")
    col1, col2 = st.columns([2,3])
    rowvalraw = worksheet.row_values(5)
    rowlen = len(data)
    with col1:
        st.table(data)

    with col2:
        with st.form("Add Log", border=True):
            st.subheader("Add Log")
            fcol1, fcol2, fcol3, fcol4, fcol5, fcol6, fcol7 = st.columns(7)
            with fcol1:
                year_input = st.number_input(
                    "Year",
                    placeholder="Enter Year",
                    min_value=2000,
                    max_value=2030,
                )


            with fcol2:
                month_input = st.number_input(
                    "month",
                    placeholder="Enter month",
                    min_value = 1,
                    max_value = 12,
                )

            with fcol3:
                day_input = st.number_input(
                    "day",
                    placeholder="Enter day",
                    min_value=1,
                    max_value=31,
                )

            with fcol4:
                ac_input = st.text_input(
                    "A/C Model",
                    placeholder="Enter A/C Model",
                )

            with fcol5:
                reg_input = st.text_input(
                    "Registration",
                    placeholder="Enter Registration",
                )

            with fcol6:
                main_input = st.text_input(
                    "Maintenance",
                    placeholder="Enter Maintenance Done",
                )

            with fcol7:
                signed_input = st.text_input(
                    "Inspected By:",
                    placeholder="Enter Inspector Name",
                )

            if st.form_submit_button(label="Update Table", type="secondary", disabled=False, use_container_width=False):
                cellrow = rowlen + 1
                yearcolumn = 1
                monthcolumn = 2
                daycolumn = 3
                accolumn = 4
                regcolumn = 5
                maincolumn = 6
                signedcolumn = 7
                worksheet.update_cell(cellrow, yearcolumn, year_input)
                worksheet.update_cell(cellrow, monthcolumn, month_input)
                worksheet.update_cell(cellrow, daycolumn, day_input)
                worksheet.update_cell(cellrow, accolumn, ac_input)
                worksheet.update_cell(cellrow, regcolumn, reg_input)
                worksheet.update_cell(cellrow, maincolumn, main_input)
                worksheet.update_cell(cellrow, signedcolumn, signed_input)
                st.success("Table Updated")