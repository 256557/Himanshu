# Writing rules for this project

- When writing any answer, solution or assessment text for the user, apply the academic-prose skill (`/anthropic-skills:academic-prose`) and run its checker (`scripts/check_prose.py`) on the text before giving it.
- Also apply the user's GitHub AI-writing skill once it is installed in the session (name and link still to be confirmed by the user).
- Verify every number in a solution by calculation or simulation before presenting it; record verified questions in `failed_questions.md` with the checking script in `verify/`.
