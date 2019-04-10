# pip install camelcase
import camelcase

camel = camelcase.CamelCase()

text = "mi name is miguel"

print(camel.hump(text)) # My Name is Miguel

# pip uninstall camelcase
# pip list