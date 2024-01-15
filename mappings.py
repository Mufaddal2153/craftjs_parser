import json
from bs4 import BeautifulSoup, Tag


def traverse_tree(
        node: Tag, 
        path: list =[], 
        depth: int =0, 
        index: int =0
    ) -> dict:
    path.append(index)
    json_node = {
        "type": node.name,
        "id": node.name + "_" + "_".join(map(str, path)),
        "attrs": dict(node.attrs),
        "depth": depth,
        "path": ",".join(map(str, path)),
        "children": [traverse_tree(child, path, depth + 1, i) for i, child in enumerate(node.find_all(recursive=False))],
    }
    path.pop()
    return json_node


def html_to_json_mapping(
        html_file: str
    ) -> dict:

    with open(html_file, "r") as file:
        html_content = file.read()
    soup = BeautifulSoup(html_content, "html.parser")
    in_body_data = soup.findChildren("body")[0]

    while in_body_data.script:
        in_body_data.script.decompose()
    
    while in_body_data.style:
        in_body_data.style.decompose()
    
    json_data = traverse_tree(in_body_data)
    return json_data

# html_to_json_mapping("test.html")