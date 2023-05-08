# This entrypoint file to be used in development. Start by reading README.md
from pytest import main

from arithmetic_arranger_r import arithmetic_arranger

print(arithmetic_arranger(["32 + 6898", "383201 - 2", "45 + 4343", "123 + 49"],True))


# Run unit tests automatically
main(['-vv'])
