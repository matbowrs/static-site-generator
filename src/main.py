import os
import shutil
from manipulate_markdown import extract_title
from markdown_blocks import markdown_to_html_node

def setup_source_destination(src, dest):
    if os.path.exists(src) and os.path.exists(dest):
        print(f"Source path {src} and destination path {dest} exist.")
        print(f"Deleting all content under {dest}") 
        shutil.rmtree(dest)
        os.mkdir(dest)
    else:
        if not os.path.exists(src) and not os.path.exists(dest):
            print(f"Neither the source ({src}) path nor the destination path ({dest}) exist.")
        elif os.path.exists(src):
            print(f"Source path {src} exists, but destination path {dest} does not. Creating...")
            os.mkdir(dest)
            if os.path.exists(dest):
                print("Path created successfully!")
        else:
            print(f"Destination path {dest} exists, but source path {src} does not.")

def copy_source_to_dest(src, dest, src_index=0):
    src_directory_contents = os.listdir(src)
    if src_index == 0:
        setup_source_destination(src, dest)

    if len(src_directory_contents) > src_index:
        if os.path.isdir(f"{src}/{src_directory_contents[src_index]}"):
            print(f"Copying dir '{src_directory_contents[src_index]}' to {dest}")
            shutil.copytree(f"{src}/{src_directory_contents[src_index]}", f"{dest}/{src_directory_contents[0]}")
        else:
            print(f"Copying file '{src_directory_contents[src_index]}' to {dest}")
            shutil.copy(f"{src}/{src_directory_contents[src_index]}", dest)

        src_index += 1
        copy_source_to_dest(src, dest, src_index)
    else:
        print("Files copied!")
        print(f"ls {dest} -> {os.listdir(dest)}")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    md_content = ""
    template_content = ""
    if os.path.exists(from_path):
        with open(from_path, encoding="utf-8") as f:
            md_content = f.read()
        print(md_content)
    if os.path.exists(template_path):
        with open(template_path, encoding="utf-8") as f:
            template_content = f.read()
        print(template_content)
    html_content = markdown_to_html_node(md_content)
    html = html_content.to_html()
    title = extract_title(md_content)
    print(template_content.replace("{{ Title }}", title))
    template_content = template_content.replace("{{ Title }}", title)
    print(template_content)
    template_content = template_content.replace("{{ Content }}", html)
    print(template_content)

    if not os.path.exists(dest_path):
        os.mkdir(dest_path)
    
    with open(f"{dest_path}/index.html", "w") as f:
        f.write(template_content)


def main():
    ssg = "/Users/matthew/workspace/github.com/matbowrs/static-site-generator"
    #copy_source_to_dest(f"{ssg}/static", f"{ssg}/public") 
    copy_source_to_dest(f"{ssg}/static", f"{ssg}/public") 
    generate_page(f"{ssg}/content/index.md", f"{ssg}/template.html", f"{ssg}/public")
    
if __name__ == "__main__":
    main()
