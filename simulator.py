from funnel import Funnel

def simulate_onboarding(customers_count):
    funnel = Funnel('config.yaml')
    results = funnel.run_funnel(customers_count)
    return results