[[software_engineering/Theory/7_Documentation_and_APIs/slides.pdf]]
# Versioning
can version the endpoints
- `*/v1/*` or `v2` ...
# Richardson Maturity level
## Level 0
only use the `http` for transport
## level 1
endpoints for resources, starting to add something fx to URL and body
## Level 2
HTTP verbs, use
- post
- put
- ...
## Level 3
hypermedia controls
- whenever you make a request you get a response
	- you also get links in the response, fx we `get` a `person` then it in the response there could also be a link to which url you would have to hit to delete the person, to list what the person has ...
### Carstens recommendations
stop at level 2, dont implement the discovery.
# Semantic versioning
major.minor.patch => fx: 0.1.4
## Major
breaking changes
## Minor 
new features
## Patch
bugfixes
# Userscentric API Design
## OPENAPI (previously SWAGGER)
Implement the discovery of the specific links.
### OpenAPI Spec
different versions, swagger implements an old one

