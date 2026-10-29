<!-- HU-STATUS TEMPLATE - do NOT remove the <!-- ... --> markers or the table headers.
     Your weekly grade is read AUTOMATICALLY from this file:
       13-week/hu-status/README.md  (inside YOUR fork). English. -->

# Weekly Status - Week 13

<!-- CONFIG-START - must match your profile repo (username/username) CONFIG -->
- FULL_NAME: Luis Fernando Claros Ramos
- GITHUB_USER: luisfclaros
- TEAM: Group 1
- SPRINT_GOAL: Map the RedFish attack surface, analyze the Internet-to-API-Gateway trust boundary, and propose verifiable security backlog items.
<!-- CONFIG-END -->

## 1. User stories worked this week
| HU ID | Title | Status (todo/doing/done) | Evidence (PR or commit URL) |
|---|---|---|---|
| SEC-W13-001 | Reject invalid and expired JWTs on protected API routes | doing | https://github.com/code-corhuila/redfish-docs/issues/4 |
| SEC-W13-002 | Limit abusive and oversized requests at the API gateway | doing | https://github.com/code-corhuila/redfish-docs/issues/5 |
| SEC-W13-003 | Minimize public health and error information | doing | https://github.com/code-corhuila/redfish-docs/issues/6 |

## 2. My individual contribution
- Claimed the Internet/external client → api-gateway boundary and documented the claim in the team documentation repository.
- Added the CP0 workshop configuration and CP1 attack-surface map to this fork.
- Opened a STRIDE pull request with six preliminary threats, risk scores, existing documented controls, and proposed mitigations.
- Opened three security backlog issues with verifiable acceptance criteria.
- Added a manual CI workflow proposal, a negative authorization test for the documented `GET /api/products` endpoint, and instructions for running the test.

## 3. Blockers and risks
- The negative authorization test has not been executed against a running RedFish test deployment; the real result must be recorded.
- The physical book's edition, year, library call number, consulted page(s), and library visit/loan record time still need to be verified and entered. Do not submit guessed bibliographic details.
- The personal reflection document must be written by me in my own words and shared with the instructor as Editor, as required by the assignment.
- The peer-review comment is still pending.

## 4. Plan for next week
- Verify the actual gateway routes, security settings, and negative-test behavior with the team.
- Complete the physical-book citation and mark the STRIDE rows that are genuinely supported by the consulted page.
- Run the security workflow against a disposable test deployment and record the result.
- Complete the student-authored reflection and peer-review evidence before the Moodle submission.

## 5. Compliance self-check
- [x] Conventional Commits - `type(scope): summary`
- [ ] Per-environment HU branch + PR to that environment (hu-xxx-dev -> develop, ...)
- [x] Testable acceptance criteria
- [x] Tests added/updated (unit / integration) — added, execution pending
- [ ] DDD / hexagonal boundaries respected (domain has no I/O) — no application code changed in this workshop
- [x] No secrets; config via environment variables

## 6. Evidence links
- Workshop folder: https://github.com/luisfclaros/sistemas-distribuidos-2026-b-g1/tree/main/13-week/workshop
- Attack surface: https://github.com/luisfclaros/sistemas-distribuidos-2026-b-g1/blob/main/13-week/workshop/01-attack-surface.md
- CP0 configuration: https://github.com/luisfclaros/sistemas-distribuidos-2026-b-g1/blob/main/13-week/workshop/README.md
- STRIDE pull request: https://github.com/code-corhuila/redfish-docs/pull/3
- Claim issue: https://github.com/code-corhuila/redfish-docs/issues/2
- Security story 1: https://github.com/code-corhuila/redfish-docs/issues/4
- Security story 2: https://github.com/code-corhuila/redfish-docs/issues/5
- Security story 3: https://github.com/code-corhuila/redfish-docs/issues/6
- CI workflow: https://github.com/luisfclaros/sistemas-distribuidos-2026-b-g1/blob/main/.github/workflows/w13-security-gate.yml
- Negative authorization test: https://github.com/luisfclaros/sistemas-distribuidos-2026-b-g1/blob/main/13-week/workshop/04-security-ci/test_negative_authorization.py
- HOW-TO-RUN: https://github.com/luisfclaros/sistemas-distribuidos-2026-b-g1/blob/main/13-week/workshop/04-security-ci/HOW-TO-RUN.md
- Reflection document: pending — student-authored and shared as Editor.
- Peer review comment: pending.
