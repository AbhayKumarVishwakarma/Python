import pandas as pd

# Define edge cases data
edge_cases = [
    ["User Delayed Response", "User resumes after 5-10 minutes", "Use caching with expiration"],
    ["User Skips a Question", "User sends blank response", "Ensure input validation before proceeding"],
    ["User Changes Answer", "User wants to modify a response", "Allow revision before finalizing"],
    ["User Repeats a Response", "User sends duplicate data", "Detect duplicates and ask for confirmation"],
    ["User Tries to Change Language", "User wants to switch mid-conversation", "Warn about restarting or allow translation"],
    ["User Inputs Invalid Phone", "Number too short/long", "Validate phone format dynamically"],
    ["User Sends Unexpected Messages", "User types 'Cancel' or 'Help'", "Handle exit/help commands properly"],
    ["CRM Submission Issues", "API down or slow", "Retry or store locally for later submission"],
    ["Network Issues", "Slow internet or API rate limits", "Queue messages instead of failing"],
    ["User Restarts After Completion", "User types 'Hi' again", "Ask if they want to start a new request"],
    ["User Uses Multiple Numbers", "Switches phone numbers", "Allow verification before resuming"],
    ["User Sends Media Instead of Text", "User sends voice note or image", "Detect and prompt for text input"],
    ["User Cancels Midway", "User wants to return later", "Allow resuming within a set time"],
    ["User Switches Languages Midway", "User types 'Deutsch' after selecting English", "Ask for confirmation before switching"],
    ["User Uses Symbols Instead of Text", "User enters '#######' as name", "Filter invalid characters"],
    ["User in Different Time Zone", "User selects 'Evening' but timezone differs", "Convert to local time or ask for specifics"]
]

# Convert to DataFrame
df = pd.DataFrame(edge_cases, columns=["Edge Case", "Description", "Solution"])

# Save to Excel
file_path = "whatsapp_edge_cases.xlsx"
df.to_excel(file_path, index=False)

# Provide file path
file_path
