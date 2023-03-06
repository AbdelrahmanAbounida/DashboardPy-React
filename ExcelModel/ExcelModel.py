import requests

class ExcelModel:

    def __init__(self):
        self.base_url = "https://aboneda2.pythonanywhere.com/api/"
        self.revenue_url = f"{self.base_url}revenues/"
        self.operationalCosts_url = f"{self.base_url}operationalCosts/"
        self.capitalInvestment_url = f"{self.base_url}capital_investments/"
        self.timeLines_url = f"{self.base_url}timelines/"
        self.others_url = f"{self.base_url}others/"
    ######################
    # Revenue
    ######################
    def get_revenues(self):
        revenue = requests.get(self.revenue_url).json()
        if len(revenue):
            revenue = revenue[0]
            volume = revenue["volume"]
            annual_volume_growth = revenue["annual_volume_growth"]
            price = revenue["price"]
            annual_price_growth = revenue["annual_price_growth"]
        
            return volume, annual_volume_growth, price, annual_price_growth
        
        print("Please check the API Connection")
        return 0,0,0,0

    def edit_revenues(self,volume,annual_volume_growth,price,annual_price_growth):
        data = {
                "volume": volume,
                "annual_volume_growth": annual_volume_growth,
                "price": price,
                "annual_price_growth": annual_price_growth
            }
        resp = requests.put(f"{self.revenue_url}/1",json=data)   
        if resp.status_code == 200:
            print("Editing Revenues Have been updated successfully")
        else:
            print("Editing Revenues failed")      

    ######################
    # operationalCosts
    ######################

    def get_operational_Costs(self):

        operationalCosts = requests.get(self.operationalCosts_url).json()
        if len(operationalCosts):
            operationalCosts = operationalCosts[0]
            cost_item1_variable = operationalCosts["cost_item1_variable"]
            cost_item2_fixed = operationalCosts["cost_item2_fixed"]
            cost_item2_annual_growth = operationalCosts["cost_item2_annual_growth"]
        
            return cost_item1_variable, cost_item2_fixed, cost_item2_annual_growth
        
        print("Please check the API Connection")
        return 0,0,0

    def edit_operational_Costs(self,cost_item1_variable,cost_item2_fixed,cost_item2_annual_growth):
        data = {
                "cost_item1_variable": cost_item1_variable,
                "cost_item2_fixed": cost_item2_fixed,
                "cost_item2_annual_growth": cost_item2_annual_growth
            }
        resp = requests.put(f"{self.operationalCosts_url}/1",json=data)   
        if resp.status_code == 200:
            print("Editing operationalCosts Have been updated successfully")
        else:
            print("Editing operationalCosts failed") 

    ######################
    # capital_investments
    ######################
    def get_capital_investments(self):
        capital_investments = requests.get(self.capitalInvestment_url).json()
        if len(capital_investments):
            capital_investments = capital_investments[0]
            project_capex_item1 = capital_investments["project_capex_item1"]
            project_capex_item2 = capital_investments["project_capex_item2"]
            total_project_capex = capital_investments["total_project_capex"]
            equity_debt = capital_investments["equity_debt"]
            debt_repayment_period = capital_investments["debt_repayment_period"]
        
            return project_capex_item1, project_capex_item2, total_project_capex,equity_debt,debt_repayment_period
        
        print("Please check the API Connection")
        return 0,0,0,0,0

    def edit_capital_investments(self,project_capex_item1, project_capex_item2, total_project_capex,equity_debt,debt_repayment_period):
        data = {
                "project_capex_item1": project_capex_item1,
                "project_capex_item2": project_capex_item2,
                "total_project_capex": total_project_capex,
                "equity_debt": equity_debt,
                "debt_repayment_period": debt_repayment_period
            }
        resp = requests.put(f"{self.capitalInvestment_url}/1",json=data)   
        if resp.status_code == 200:
            print("Editing capital_investments Have been updated successfully")
        else:
            print("Editing capital_investments failed") 

        
    ######################
    # Timeline
    ######################
    def get_timelines(self):
        timelines = requests.get(self.timeLines_url).json()
        if len(timelines):
            timelines = timelines[0]
            start_capex = timelines["start_capex"]
            end_capex = timelines["end_capex"]
            start_operations = timelines["start_operations"]
            asset_life = timelines["asset_life"]
        
            return start_capex, end_capex, start_operations,asset_life
        
        print("Please check the API Connection")
        return 0,0,0,0

    def edit_timelines(self,start_capex, end_capex, start_operations,asset_life):
        data = {
                "start_capex": start_capex,
                "end_capex": end_capex,
                "start_operations": start_operations,
                "asset_life": asset_life
            }
        resp = requests.put(f"{self.timeLines_url}/1",json=data)   
        if resp.status_code == 200:
            print("Editing timelines Have been updated successfully")
        else:
            print("Editing timelines failed") 

    ######################
    # Others
    ######################
    def get_others(self):
        timelines = requests.get(self.others_url).json()
        if len(timelines):
            timelines = timelines[0]
            income_tax_rate = timelines["income_tax_rate"]
            interst_rate_debt = timelines["interst_rate_debt"]
            return income_tax_rate, interst_rate_debt
        
        print("Please check the API Connection")
        return 0,0

    def edit_otherss(self,income_tax_rate,interst_rate_debt):
        data = {
                "income_tax_rate": income_tax_rate,
                "interst_rate_debt": interst_rate_debt
            }
        resp = requests.put(f"{self.others_url}/1",json=data)   
        if resp.status_code == 200:
            print("Editing others Have been updated successfully")
        else:
            print("Editing others failed")


if __name__ == '__main__':
    model = ExcelModel()

    ## 1 - Revenues
    volume, annual_volume_growth, price, annual_price_growth = model.get_revenues()
    volume = 123120
    # model.edit_revenues(volume, annual_volume_growth, price, annual_price_growth)

    print( model.get_others())



