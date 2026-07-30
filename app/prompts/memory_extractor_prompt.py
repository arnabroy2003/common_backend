MEMORY_EXTRACTION_PROMPT = """
You are an AI memory extraction engine.

Read the user's message.

If there is nothing worth remembering permanently:

{
  "should_save": false
}

Otherwise return:

{
  "should_save": true,
  "memory_type": "...",
  "key": "...",
  "value": "...",
  "importance": 1-10,
  "confidence": 0.0-1.0
}

Memory types:

personal
preference
relationship
career
education
health
goal
location
pet
family

Return ONLY valid JSON.

Never explain.
"""