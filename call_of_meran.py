import os

def Installation_commands():
    calling_of_libs=['@mui/material','@emotion/react','@emotion/styled','@reduxjs/toolkit','redux','motion','-D tailwindcss@3']
    for lib in range(len(calling_of_libs)):
      print(f"\nINSTALLING {calling_of_libs[lib]} LIBRARY\n")
      os.system("npm install "+calling_of_libs[lib])
      if calling_of_libs[lib] == '-D tailwindcss@3':
          print("index initalization procces")
          os.system("npx tailwindcss init")
          with open('tailwind.config.js','w') as work_on:
              work_on.write("""
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
""")
              work_on.close()
          print("\nDONE")
      print("\nLIBRARY INSTALLED")

def write_command(com):
    return os.system(com)

def change_path(dir):
    return os.chdir(dir)

def create_path(dir):
    return os.mkdir(dir)



def src_defult_content():
    print("changeing the src content")
    return"""
import logo from './logo.svg';
import './App.css';

function App() {
  return (
   <main>
     <h1 className="text-3xl font-bold underline">
      Hello world!
    </h1>
    <h3 className="title">this is the app ROOT</h3>
   </main>
  );
}

export default App;


"""

def comp_obj_default_content(num):
    function_content="{"+f"""
 return (
    <div className="comp_model">
      <h1>comp number {str(num)}</h1>
      <p>This is a functional component.</p>
    </div>
  );
"""+"}"
    print("adding COMPUNENT defualt content")
    return f"""
import React from 'react';

function CompNumber{str(num)} () {function_content}
\n\n

export default CompNumber{str(num)}
"""



def Page_default_content(num):
    page_content="{"+f"""
 return (
    <div>
      <h1>Page {str(num)}</h1>
      <p>Welcome to the page {str(num)}</p>
    </div>
  );
"""+"}"
    print("adding PAGE defualt content")
    return "{"+f"""
import React from 'react';

const Page{str(num)} = () => {
 page_content
};

export default Page{str(num)};
"""+"}"



while True:
    project_tech_type=input("select the project type (R:react)(A:angular)......(x:exit):")
    project_name=input("wrtie the project name:")
    project_comps=int(input("add amount of compounents:")) 
    project_pages=int(input("add amount of Pages:")) 
    write_command("node --v")
    if project_tech_type =="r" or project_tech_type =="R" :
      write_command(f"npx create-react-app {project_name}")
      change_path(project_name)
      comp_model=open(f"src/App.js",'w')
      comp_model.write(src_defult_content())
      comp_model.close()

      for c in range(project_comps):
          create_path(f"src/CompNumber{str(c)}")
          write_command(f"nul>src/CompNumber{str(c)}/comp_obj.js")
          write_command(f"nul>src/CompNumber{str(c)}/style.css")
          comp_model=open(f"src/CompNumber{str(c)}/comp_obj.js",'w')
          comp_model.write(comp_obj_default_content(c))
          comp_model.close()
          #change_path("..")
      for p in range(project_pages):
          create_path(f"src/Page{str(p)}")
          write_command(f"nul>src/Page{str(p)}/page_obj.js")
          write_command(f"nul>src/Page{str(p)}/style.css")
          page_model=open(f"src/Page{str(p)}/page_obj.js",'w')
          page_model.write(Page_default_content(p))
          page_model.close()
          #change_path("..")
      Installation_commands()
      write_command("npm start")

      change_path("..")

    elif project_tech_type =="a" or project_tech_type =="A" :
      print("not avilable")
    else:break






node_command=os.path.exists("node")

if node_command :
    print("found")
else:
    print("no its not")