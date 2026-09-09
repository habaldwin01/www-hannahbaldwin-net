
from flask import Blueprint, request, render_template, Response, make_response, send_file
import markdown
import os
from pygments.formatters import HtmlFormatter

site_pages = Blueprint("site_pages", __name__)

def markdown_page(path):
    if path.endswith(".md"):
        path = path[:-3]
    split_path = path.split("/")
    sanit_path = ""
    for ele in split_path:
        sanit_path = sanit_path + "/" + to_snake_case(ele)

    raw_markdown = None

    blog_path = "blog" + sanit_path
    blog_path = blog_path.replace("_", "-")

    #print(blog_path)

    if os.path.isfile(blog_path + ".md"):
        with open(blog_path + ".md") as f:
            raw_markdown = f.read()
    elif os.path.isfile(blog_path + "/index.md"):
        with open(blog_path + "/index.md") as f:
            raw_markdown = f.read()

    if raw_markdown is None:
        return render_template("404.html")

    md_template_string = markdown.markdown(
        raw_markdown, extensions=[
            "markdown.extensions.extra",
            "markdown.extensions.codehilite",
            "markdown.extensions.sane_lists"
        ]
    )
    md_template_string = md_template_string.replace("<table>", "<table class=\"table table-hover\">")
    formatter = HtmlFormatter(style="emacs",full=True,cssclass="codehilite")
    css_string = formatter.get_style_defs()
    md_css_string = "<style>" + css_string + "</style>"
    md_template_string = md_template_string.replace("<div class=\"codehilite\">", "<div class=\"codehilite container p-2 my-3 border rounded\">")
    md_template_string = md_template_string.replace("<pre>", "<pre style=\"margin:0;\">")
    md_template = md_css_string + md_template_string

    return render_template("blog_page.html", markdown=md_template)

@blogumentation_pages.route("/blog", defaults={'path': 'index'}, methods=['GET'])
@blogumentation_pages.route("/blog/", defaults={'path': 'index'}, methods=['GET'])
@blogumentation_pages.route("/blog/<path:path>", methods=['GET'])
def blogs_index(path):
    return markdown_page(path)

