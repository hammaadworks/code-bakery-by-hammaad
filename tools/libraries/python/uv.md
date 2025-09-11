uv
run <script> = run the script with .venv and batteries 
init = batteries on exisiting project
init --app <package> = new app
add <package> = add packages
add -r requirements.txt = install all existing packages
tree = list the dependency tree
remove <package> = remove a package
sync = sync up from the uv.lock file

uvx <package> = install a system wide package a.k.a tool
uv tool run ruff
uv tool install ruff
uv tool remove <tool>
