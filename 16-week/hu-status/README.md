<!-- HU-STATUS TEMPLATE - do NOT remove the <!-- ... --> markers or the table headers.
# Weekly Status - Week 16
<!-- CONFIG-START - must match your profile repo (username/username) CONFIG -->
- FULL_NAME: Luis Fernando Claros Ramos
- GITHUB_USER: luisfclaros
- TEAM: Group 1
- SPRINT_GOAL: Integrate RedFish MVP 3 functionality, verify the local system, and prepare the final technical demonstration and delivery.
<!-- CONFIG-END -->
## 1. User stories worked this week
| HU ID | Title | Status (todo/doing/done) | Evidence (PR or commit URL) |
|---|---|---|---|
| MVP3-W16-001 | Integrate production, inventory, commercial, dispatch, and administration workflows in the RedFish application | doing | https://github.com/luisfclaros/RedFish/pull/50 |
| MVP3-W16-002 | Verify local startup, authentication, health, and key operational workflows | done | https://github.com/luisfclaros/RedFish/pull/50 |
| MVP3-W16-003 | Prepare the final MVP 3 release, documentation, and demonstration package | doing | https://github.com/luisfclaros/RedFish/pull/50 |
## 2. My individual contribution
- Integrated the main application workflows: products and customers; ponds and feeding; inventory entries, exits, and movement history; orders and stock reservations; and dispatch scheduling, transit, and delivery.
- Integrated role-based access for Administration, Production, Operations, and Commercial, with users stored in MySQL and BCrypt password hashing.
- Corrected interface and operational issues found during local use, including readable inventory/product names, date presentation, safe handling of insufficient stock, and records with dependencies.
- Rebuilt and started the application with Docker Compose on the local Windows environment. The application and MySQL became available, the health endpoint reported UP after startup, and local login was confirmed by the developer.
- Prepared the integration work in PR #50 without directly modifying main, Develop, or Qa.
## 3. Blockers and risks
- PR #50 remains open and in draft; this report does not claim it has been merged or released from main.
- Moodle MVP 3 release requirements still need a confirmed v3.0.0 tag on main, updated CHANGELOG and ADRs, and final release evidence.
- The required live demonstration must include a simulated failure and show gradual degradation; that demonstration evidence is not recorded here.
- The current executable implementation is a Spring Boot modular monolith with MySQL. The target microservices architecture must be presented as a target, not as a deployed fact.
## 4. Plan for next week
- Finish the release gate: review and promote approved PRs through the required Git environments, verify the tag and release notes, and capture final demo evidence.
- Complete the presentation and user/administrator operating instructions.
## 5. Compliance self-check
- [x] Conventional Commits used in related implementation work
- [x] Integration work kept in the dedicated branch and PR
- [x] Core application workflows implemented and locally checked
- [ ] PR #50 merged and release promoted to main
- [ ] Tag v3.0.0 and CHANGELOG verified
- [ ] Live demonstration with simulated failure recorded
- [x] No secrets or local environment files committed
## 6. Evidence links
- Integrated MVP 3 PR: https://github.com/luisfclaros/RedFish/pull/50
- Week 15 load/resilience preparation: https://github.com/luisfclaros/RedFish/pull/51
- Documentation repository: https://github.com/code-corhuila/redfish-docs
