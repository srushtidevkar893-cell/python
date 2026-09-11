def price_engine(asset_costs):
    # Sort costs from highest to lowest
    sorted_costs = sorted(asset_costs, reverse=True)

    # Get top 3 priciest entries
    top_three = sorted_costs[:3]

    print("Top 3 Priciest Assets:")
    for cost in top_three:
        print(cost)


# Example asset costs
asset_costs = [125.50, 890.75, 450.25, 1200.00, 675.80, 999.99]

price_engine(asset_costs)