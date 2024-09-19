amount_to_convert = 500
nz_to_aus_rate = 0.95
nz_dollars = amount_to_convert

# NZ dollars to Australian dollars conversion
aus_dollars = nz_dollars * nz_to_aus_rate
print("NZ $", nz_dollars, "- AUS $", aus_dollars, sep="")

# Australian dollars to New Zealand dollars conversion
nz_dollars = aus_dollars / nz_to_aus_rate 
print("AUS $", aus_dollars, " - NZ $", nz_dollars, sep="")
