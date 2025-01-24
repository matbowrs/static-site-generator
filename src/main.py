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

def generate_page_recursive(dir_path_content, template_path, dest_dir_path):
    dirs = []
    files_to_process = []
    dir_contents = os.listdir(dir_path_content)

    for item in dir_contents:
        print(item)
        if os.path.isdir(f"{dir_path_content}/{item}"):
            dirs.append(item)
        elif os.path.isfile(f"{dir_path_content}/{item}"):
            files_to_process.append(item)
        else:
            raise TypeError("Item was not a file, nor a directory. Could not process.")

    print(f"dirs: {dirs}")
    print(f"files: {files_to_process}")
    # Generate page
    if files_to_process:
        for file in files_to_process:
            md_content = ""
            template_content = ""
            with open(f"{dir_path_content}/{file}", encoding="utf-8") as f:
                md_content = f.read()
            #print(md_content)
            
            if os.path.exists(template_path):
                with open(template_path, encoding="utf-8") as f:
                    template_content = f.read()
            #    print(template_content)

            html_content = markdown_to_html_node(md_content)
            html = html_content.to_html()
            title = extract_title(md_content)
            #print(template_content.replace("{{ Title }}", title))
            template_content = template_content.replace("{{ Title }}", title)
            #print(template_content)
            template_content = template_content.replace("{{ Content }}", html)
            #print(template_content)
    

            if os.path.exists(f"{dest_dir_path}/index.html"):
                print(f"index.html file found! Creating new one under the parent dir...")
                parent_dir = dir_path_content.split("/")[-1]
                os.mkdir(f"{dest_dir_path}/{parent_dir}")
                print(f"parent_dir: {parent_dir}")
                with open(f"{dest_dir_path}/{parent_dir}/index.html", "w") as f:
                    f.write(template_content)
            else:
                print(f"No index.html file created yet! Creating...")
                if not os.path.exists(dest_dir_path):
                    os.mkdir(dest_dir_path)
                with open(f"{dest_dir_path}/index.html", "w") as f:
                    f.write(template_content)

            files_to_process.pop(0)
    
    if dirs:
        generate_page_recursive(f"{dir_path_content}/{dirs[0]}", template_path, dest_dir_path)
def main():
    ssg = "/Users/matthew/workspace/github.com/matbowrs/static-site-generator"
    #copy_source_to_dest(f"{ssg}/static", f"{ssg}/public") 
    copy_source_to_dest(f"{ssg}/static", f"{ssg}/public") 
    generate_page_recursive(f"{ssg}/content", f"{ssg}/template.html", f"{ssg}/public")
    
if __name__ == "__main__":
    main()
