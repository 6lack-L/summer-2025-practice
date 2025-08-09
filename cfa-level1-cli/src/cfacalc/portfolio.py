class Portfolio:
    def __init__(self, assets=None):
        if assets is None:
            assets = []
        self.assets = assets

    def add_asset(self, asset):
        self.assets.append(asset)

    def remove_asset(self, asset):
        self.assets.remove(asset)

    def total_value(self):
        return sum(asset['value'] for asset in self.assets)

    def expected_return(self):
        total_return = sum(asset['value'] * asset['expected_return'] for asset in self.assets)
        return total_return / self.total_value() if self.total_value() > 0 else 0

    def risk_assessment(self):
        total_variance = sum(asset['value'] * (asset['risk'] ** 2) for asset in self.assets)
        return total_variance / self.total_value() if self.total_value() > 0 else 0

    def asset_allocation(self):
        allocation = {asset['name']: asset['value'] / self.total_value() for asset in self.assets}
        return allocation if self.total_value() > 0 else {}