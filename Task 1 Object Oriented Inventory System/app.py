import streamlit as st
from inventory import Inventory, Product

# PAGE CONFIG
st.set_page_config(page_title="Inventory Hub", page_icon="📦", layout="wide")

# CUSTOM CSS
st.markdown("""
<style>
.stApp {
    background: #f5f8fd;
}
header {
    visibility: hidden;
}
footer {
    visibility: hidden;
}
#MainMenu {
    visibility: hidden;
}
.block-container {
    max-width: 1500px;
    padding-top: 0.5rem;
    padding-bottom: 2rem;
}
.navbar {
    background: #17243f;
    padding: 16px 30px;
    margin: -10px -50px 30px -50px;
    min-height: 72px;
    display: flex;
    align-items: center;
}
.brand {
    display: flex;
    align-items: center;
    gap: 12px;
}
.brand-icon {
    font-size: 34px;
}
.brand-name {
    color: white;
    font-size: 21px;
    font-weight: 750;
}
.brand-separator {
    color: #65738c;
    font-size: 20px;
    margin: 0 3px;
}
.brand-subtitle {
    color: #aeb8c9;
    font-size: 13px;
}
div.stButton > button {
    border: none;
    border-radius: 9px;
    background: transparent;
    color: #263653;
    font-weight: 600;
    font-size: 14px;
    min-height: 42px;
}
div.stButton > button:hover {
    background: #e5edfb;
    color: #2459c4;
}
.hero {
    background: linear-gradient(105deg, #edf5ff, #f5f8ff 70%, #e8f0ff);
    border: 1px solid #d6e4fa;
    border-radius: 14px;
    padding: 27px 35px;
    min-height: 120px;
    margin-bottom: 25px;
    position: relative;
    overflow: hidden;
}
.hero-icon {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 68px;
    height: 68px;
    background: #d9e7ff;
    border-radius: 15px;
    font-size: 38px;
    vertical-align: middle;
    margin-right: 20px;
}
.hero-text {
    display: inline-block;
    vertical-align: middle;
}
.hero-title {
    color: #182743;
    font-size: 31px;
    font-weight: 750;
    margin-bottom: 5px;
}
.hero-description {
    color: #687998;
    font-size: 14px;
}
.hero-package {
    position: absolute;
    right: 70px;
    top: 27px;
    font-size: 62px;
}
.card-header {
    background: linear-gradient(105deg, #edf5ff, #f5f8ff);
    border-bottom: 1px solid #dfe8f6;
    padding: 18px 22px;
    margin: -1px -1px 22px -1px;
    border-radius: 12px 12px 0 0;
}
.card-title {
    color: #1a2946;
    font-size: 18px;
    font-weight: 750;
}
.card-description {
    color: #6b7b9b;
    font-size: 13px;
    margin-top: 5px;
}
.stTextInput label,
.stNumberInput label {
    color: #253550 !important;
    font-weight: 700 !important;
    font-size: 14px !important;
}
div[data-baseweb="input"] {
    border: 1px solid #d5dfed;
    border-radius: 9px;
    background: white;
}
div[data-baseweb="input"]:focus-within {
    border-color: #4c75ce;
    box-shadow: 0 0 0 2px rgba(76, 117, 206, 0.10);
}
.main-update-button {
    margin-top: 20px;
}
.main-update-button div.stButton > button {
    background: #285fd1 !important;
    color: white !important;
    border: none !important;
    width: 275px;
    height: 52px;
    border-radius: 9px;
    font-size: 15px;
    font-weight: 750;
    box-shadow: 0 5px 13px rgba(40, 95, 209, 0.20);
}
.main-update-button div.stButton > button:hover {
    background: #1e50bd !important;
    color: white !important;
}
.footer {
    text-align: center;
    color: #8d9ab0;
    font-size: 12px;
    margin-top: 28px;
}
</style>
""", unsafe_allow_html=True)

# INVENTORY
inventory = Inventory()

# PAGE STATE
if "page" not in st.session_state:
    st.session_state.page = "Dashboard"

# NAVIGATION FUNCTION
def change_page(page):
    st.session_state.page = page

# NAVBAR
st.markdown("""
<div class="navbar">
    <div class="brand">
        <span class="brand-icon">📦</span>
        <span class="brand-name">Inventory Hub</span>
        <span class="brand-separator">|</span>
        <span class="brand-subtitle">Inventory Management System</span>
    </div>
</div>
""", unsafe_allow_html=True)

# NAVIGATION
nav1, nav2, nav3, nav4, nav5, nav6 = st.columns([1.05, 1.15, 1.35, 1.30, 1.25, 1.45])

with nav1:
    if st.button("⌂  Dashboard", use_container_width=True, key="nav_dashboard"):
        change_page("Dashboard")
        st.rerun()
with nav2:
    if st.button("＋  Add Product", use_container_width=True, key="nav_add_product"):
        change_page("Add Product")
        st.rerun()
with nav3:
    if st.button("✎  Update Product", use_container_width=True, key="nav_update_product"):
        change_page("Update Product")
        st.rerun()
with nav4:
    if st.button("▢  Remove Product", use_container_width=True, key="nav_remove_product"):
        change_page("Remove Product")
        st.rerun()
with nav5:
    if st.button("⌕  Search Product", use_container_width=True, key="nav_search_product"):
        change_page("Search Product")
        st.rerun()
with nav6:
    if st.button("▤  Inventory Records", use_container_width=True, key="nav_inventory_records"):
        change_page("Inventory Records")
        st.rerun()
st.markdown("<br>", unsafe_allow_html=True)

# UPDATE PRODUCT
if st.session_state.page == "Update Product":

    st.markdown("""
    <div class="hero">
        <span class="hero-icon">✎</span>
        <span class="hero-text">
            <div class="hero-title">Update Product</div>
            <div class="hero-description">
                Modify existing product details and stock information.
            </div>
        </span>
        <span class="hero-package">📦</span>
    </div>
    """, unsafe_allow_html=True)


    left, right = st.columns([0.9, 1.4], gap="large")


    # FIND PRODUCT
    with left:

        with st.container(border=True):

            st.markdown("""
            <div class="card-title">📦 &nbsp; Find Product</div>
            <div class="card-description">
                Select the product you want to update.
            </div>
            """, unsafe_allow_html=True)

            product_ids = [
                p.product_id
                for p in inventory.get_all_products()
            ]

            product_id = st.selectbox(
                "Product ID *",
                ["Select Product ID"] + product_ids
            )


    # UPDATE INFORMATION
    with right:

        with st.container(border=True):

            st.markdown("""
            <div class="card-title">✎ &nbsp; Update Information</div>
            <div class="card-description">
                Leave fields unchanged if you don't want to update them.
            </div>
            """, unsafe_allow_html=True)


            col1, col2 = st.columns(2)


            with col1:

                new_name = st.selectbox(
                    "New Product Name",
                    [
                        "select new product",
                        "Laptop",
                        "Mobile",
                        "Tablet",
                        "Sunglasses",
                        "Rice",
                        "Fry Pan",
                        "Printer",
                        "NoteBook",
                        "Hoodie",
                        "Jeans"
                    ]
                )


            with col2:

                new_category = st.selectbox(
                    "New Category",
                    [
                        "select new category",
                        "Electronics",
                        "Accessories",
                        "Grocery",
                        "Home & Kitchen",
                        "Office Supplies",
                        "Stationery",
                        "Clothing"
                    ]
                )


            col1, col2 = st.columns(2)


            with col1:

                new_price = st.number_input(
                    "New Price (Rs.)",
                    min_value=0.0,
                    value=0.0,
                    step=100.0,
                    format="%.2f"
                )


            with col2:

                new_quantity = st.number_input(
                    "New Quantity",
                    min_value=0,
                    value=0,
                    step=1
                )


    # UPDATE BUTTON
    st.markdown(
        '<div class="main-update-button">',
        unsafe_allow_html=True
    )


    if st.button(
        "✎   Update Product        →",
        key="update_button",
        use_container_width=True
    ):

        if product_id == "Select Product ID":

            st.error("Please select a Product ID.")

        else:

            kwargs = {}


            if new_name != "No Change":
                kwargs["name"] = new_name


            if new_category != "No Change":
                kwargs["category"] = new_category


            if new_price > 0:
                kwargs["price"] = new_price


            if new_quantity > 0:
                kwargs["quantity"] = new_quantity


            if not kwargs:

                st.warning(
                    "Please select or enter at least one field to update."
                )

            else:

                success, message = inventory.update_product(
                    product_id,
                    **kwargs
                )


                if success:

                    st.success(message)
                    # st.rerun()

                else:

                    st.error(message)


    st.markdown("</div>", unsafe_allow_html=True)

# DASHBOARD
elif st.session_state.page == "Dashboard":
    summary = inventory.get_summary()
    st.markdown("""
<div class="hero">
    <span class="hero-icon">📊</span>
    <span class="hero-text">
        <div class="hero-title">Inventory Dashboard</div>
        <div class="hero-description">Monitor products, stock levels, and inventory performance.</div>
    </span>
    <span class="hero-package">📦</span>
</div>
""", unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Total Products", summary["total_products"])
    c2.metric("Total Quantity", summary["total_quantity"])
    c3.metric("Categories", summary["total_categories"])
    c4.metric("Inventory Value", f'Rs. {summary["total_value"]:,.0f}')

# ADD PRODUCT
elif st.session_state.page == "Add Product":

    st.markdown("""
    <div class="hero">
        <span class="hero-icon">＋</span>
        <span class="hero-text">
            <div class="hero-title">Add Product</div>
            <div class="hero-description">
                Add a new product to your inventory.
            </div>
        </span>
        <span class="hero-package">📦</span>
    </div>
    """, unsafe_allow_html=True)

    with st.container(border=True):

        col1, col2 = st.columns(2)

        with col1:

            product_id = st.text_input(
                "Product ID *",
                placeholder="e.g. P003"
            )

            name = st.selectbox(
                "Product Name *",
                [
                    "Select Product",
                    "Laptop",
                    "Mobile",
                    "Tablet",
                    "Sunglasses",
                    "Rice",
                    "Fry Pan",
                    "Printer",
                    "NoteBook",
                    "Hoodie",
                    "Jeans"
                ]
            )

            category = st.selectbox(
                "Category *",
                [
                    "Select Category",
                    "Electronics",
                    "Accessories",
                    "Grocery",
                    "Home & Kitchen",
                    "Office Supplies",
                    "Stationery",
                    "Clothing"
                ]
            )

        with col2:

            price = st.number_input(
                "Price (Rs.) *",
                min_value=0.0,
                step=100.0
            )

            quantity = st.number_input(
                "Quantity *",
                min_value=0,
                step=1
            )

        if st.button(
            "＋  Add Product",
            use_container_width=True,
            key="add_product_button"
        ):

            if name == "Select Product":
                st.error("Please select a product name.")

            elif category == "Select Category":
                st.error("Please select a category.")

            else:

                product = Product(
                    product_id,
                    name,
                    category,
                    price,
                    quantity
                )

                success, message = inventory.add_product(product)

                if success:
                    st.success(message)
                    # st.rerun()

                else:
                    st.error(message)

# REMOVE PRODUCT
elif st.session_state.page == "Remove Product":
    st.markdown("""
<div class="hero">
    <span class="hero-icon">🗑️</span>
    <span class="hero-text">
        <div class="hero-title">Remove Product</div>
        <div class="hero-description">Remove an existing product from your inventory.</div>
    </span>
</div>
""", unsafe_allow_html=True)
    with st.container(border=True):
        product_id = st.text_input("Product ID", placeholder="e.g. P001")
        if st.button("🗑️  Remove Product", use_container_width=True, key="remove_product_button"):
            success, message = inventory.remove_product(product_id)
            if success:
                st.success(message)
                # st.rerun()
            else:
                st.error(message)

# SEARCH PRODUCT
elif st.session_state.page == "Search Product":
    st.markdown("""
<div class="hero">
    <span class="hero-icon">⌕</span>
    <span class="hero-text">
        <div class="hero-title">Search Product</div>
        <div class="hero-description">Find products by ID, name, or category.</div>
    </span>
</div>
""", unsafe_allow_html=True)
    with st.container(border=True):
        keyword = st.text_input("Search", placeholder="Enter product ID, name, or category...")
        if st.button("⌕  Search Product", use_container_width=True, key="search_product_button"):
            results = inventory.search_product(keyword)
            if results:
                data = [product.to_dict() for product in results]
                st.success(f"{len(results)} product(s) found.")
                st.dataframe(data, use_container_width=True, hide_index=True)
            else:
                st.warning("No matching products found.")

# INVENTORY RECORDS
elif st.session_state.page == "Inventory Records":
    st.markdown("""
<div class="hero">
    <span class="hero-icon">▤</span>
    <span class="hero-text">
        <div class="hero-title">Inventory Records</div>
        <div class="hero-description">View and monitor all products currently stored.</div>
    </span>
    <span class="hero-package">📦</span>
</div>
""", unsafe_allow_html=True)
    products = inventory.get_all_products()
    if products:
        data = [
    {
        "product_id": product.product_id,
        "name": product.name,
        "category": product.category,
        "price": product.price,
        "quantity": product.quantity,
        "total_value": product.total_value()
    }
    for product in products
] 
        st.dataframe(data, use_container_width=True, hide_index=True)
        st.caption(f"Showing {len(products)} product(s)")
    else:
        st.info("No inventory records available.")

# FOOTER
st.markdown("""
<div class="footer">
    Inventory Hub • Object-Oriented Inventory System • Python + Streamlit
</div>
""", unsafe_allow_html=True)
