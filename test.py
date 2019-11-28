from database import Database
import json
build = []
extract = {}
edits = []
with open('graph_build.json') as file:
    build_j = json.load(file)
    #print(build_j)
    build = build_j
with open('img_extract.json') as file:
    build_j = json.load(file)
    #print(build_j)
    extract = build_j
with open('graph_edits.json') as file:
    build_j = json.load(file)
    #print(build_j)
    edits = build_j
#data_str = json.dumps(data_dict)
# Initial graph
#build = [("core", None), ("A", "core"), ("B", "core"), ("C", "core"), ("C1", "C")]
# Extract
#extract = {"img001": ["A"], "img002": ["C1"]}
# Graph edits
#edits = [("A1", "A"), ("A2", "A")]

# Get status (this is only an example, test your code as you please as long as it works)
status = {}
if len(build) > 0:
    # Build graph
    db = Database(build[0][0])
    if len(build) > 1:
    	db.add_nodes(build[1:])
    # Add extract
    db.add_extract(extract)
    # Graph edits
    db.add_nodes(edits)
    # Update status
    status = db.get_extract_status()
    #print(db.graph)
#print(status)

print()
print()
result = {}
with open('expected_status.json') as file:
    build_j = json.load(file)
    #print(build_j)
    result = build_j
    print(build_j)
    
print(result==status)
#print(status[0])
