# Week 13 Threat Modeling Workshop

<!-- CONFIG-START -->
- FULL_NAME: Luis Fernando Claros Ramos
- GITHUB_USER: luisfclaros
- TEAM: Group 1
- DOCS_REPO: https://github.com/code-corhuila/redfish-docs
- BOUNDARY: Internet / external client → api-gateway (port 8080)
- CLAIM_ISSUE: https://github.com/code-corhuila/redfish-docs/issues/2
- REFLECTION_DOC: PENDING — create your own reflection document and share it with the instructor as Editor
- LIBRARY_BOOK: Bernd Bruegge and Allen H. Dutoit, Ingeniería de software orientado a objetos; edition, year, call number and consulted pages PENDING verification from the physical copy/catalog
- LIBRARY_RECORD_TIME: PENDING — enter the actual time recorded by CORHUILA library
<!-- CONFIG-END -->

## CP0 — Boundary claim

The claimed boundary is the Internet/external client to the RedFish API Gateway on port 8080. It is the system's public entry point, so this workshop will examine how incoming requests are authenticated, routed, validated, and protected against abuse.

## Scope and evidence

- Claim issue: [Threat model: Internet to api-gateway](https://github.com/code-corhuila/redfish-docs/issues/2)
- Architecture source: [RedFish architecture overview](https://github.com/code-corhuila/redfish-docs/blob/main/05-architecture/overview.md)
- API Gateway contract: [api-gateway OpenAPI contract](https://github.com/code-corhuila/redfish-docs/blob/main/07-api/contracts/openapi/api-gateway.yaml)

> Before final submission, verify the book's edition, publication year, library call number, consulted pages, and actual library visit/loan record. Do not invent these details. The reflection must be written by the student in their own words, as required by the assignment.
