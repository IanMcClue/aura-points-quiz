import streamlit.components.v1 as components

_COPY_LINK_JS = """
<script>
function copyLinkToClipboard(event) {
    event.preventDefault();
    const link = event.target.href;
    navigator.clipboard.writeText(link)
        .then(() => {
            alert("Link copied to clipboard!");
        })
        .catch((err) => {
            console.error("Failed to copy link: ", err);
        });
}

window.addEventListener("load", () => {
    const links = document.querySelectorAll(".copy-link");
    links.forEach((link) => {
        link.addEventListener("click", copyLinkToClipboard);
    });
});
</script>
"""

def copy_link_component():
    components.html(_COPY_LINK_JS, height=0, width=0)
