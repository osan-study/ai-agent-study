import os
import subprocess

from langgraph.graph.state import CompiledStateGraph


def visualize_graph(app: CompiledStateGraph, file_path: str):

  filename_with_ext = os.path.basename(file_path)
  filename_no_ext, _ = os.path.splitext(filename_with_ext)



  with open(f'{filename_no_ext}.mmd', "w", encoding="utf-8") as f:
    f.write(app.get_graph().draw_mermaid())


  subprocess.run(f'mmdc -i {filename_no_ext}.mmd -o {filename_no_ext}.png', shell=True)
  subprocess.run(f'open ./{filename_no_ext}.png', shell=True)



