browsing_history = []
browsing_history.append("google.com")
browsing_history.append("semicolon.africa")
browsing_history.append("linkedIn.com")
#browsing_history.pop()
print(browsing_history)
print(f"redirecting to {browsing_history[-1]}")
browsing_history.pop()
print(f"redirecting to {browsing_history[-1]}")
if not browsing_history:
