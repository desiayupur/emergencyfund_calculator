def get_job_category():
    print("Select your employment status:")
    print("1. Permanen Employee")
    print("2. Contract Employee")
    print("3. Self-employed")

    while True:
        choice = input("Enter options (1/2/3): ").strip()
        if choice in ['1', '2', '3']:
            return int(choice)
        else:
            print("⚠️ Invalid selection. Please enter 1, 2, or 3.")

def get_months_required(job_status, dependents):
    if job_status == 1:  # Permanent
        return 6 if dependents >= 1 else 3
    elif job_status == 2:  # Kontrak
        return 9 if dependents >= 1 else 6
    elif job_status == 3:  # Wirausaha
        return 12 if dependents >= 1 else 9

def format_rupiah(amount):
    return f"Rp {amount:,.0f}".replace(',', '.')

def main():
    print("\n>>>>> EMERGENCY FUND CALCULATOR <<<<<\n")

    try:
        spending = float(input("How much do you spend on regular expenses each month? (Including dependents, if any, e.g: 4500000): "))
        job_status = get_job_category()
        dependents = int(input("How many dependents do you support? For example, wife, one children, mother, so you enter 3, and so on: "))
    except ValueError:
        print("⚠️ Invalid input. Please enter a number.")
        return

    month_emergency = get_months_required(job_status, dependents)
    total_emergency = spending * month_emergency

    print("\n📊 Emergency Fund Recommendations:")
    print(f"- Monthly expenses: {format_rupiah(spending)}")
    print(f"- Recommended number of months of reserves: {month_emergency} Months")
    print(f"=> Recommended emergency fund: {format_rupiah(total_emergency)}")

    print("\n💰 Let's simulate saving for an emergency fund! ")
    print("1. I know the nominal amount that can be saved per month → so please calculate how many months it will take")
    print("2. I have a time target → so please calculate how much I should save per month")
    print("0. Skip the simulation")

    sim_choice = input("Select the simulation type (1/2/0): ").strip()

    if sim_choice == "1":
        try:
            nominal_saving = float(input("How much monthly savings can you set aside to build up an emergency fund? "))
            if nominal_saving > 0:
                reach_month = total_emergency / nominal_saving
                print(f"➡️ By saving {format_rupiah(nominal_saving)} per month, the target will be achieved in ± {reach_month:.1f} months.")
            else:
                print("⚠️ The nominal must be more than 0.")
        except ValueError:
            print("⚠️ Invalid input. Enter a number.")

    elif sim_choice == "2":
        try:
            target_month = float(input("In how many months do you want to achieve this emergency fund savings? "))
            if target_month > 0:
                saving_per_month = total_emergency / target_month
                print(f"➡️ You need to save around {format_rupiah(saving_per_month)} per month to achieve the target in {target_month:.1f} months.")
            else:
                print("⚠️ Month target must be more than 0.")
        except ValueError:
            print("⚠️ Invalid input. Enter a number.")

    elif sim_choice == "0":
        print("Saving simulation skipped.")

    else:
        print("⚠️ Invalid selection. Skip the simulation.")


    print("\n✅ Thank you for starting to think about building an emergency fund! Preparing an emergency fund is something we can control to maintain consumption smoothing from month to month amidst an uncertain future. Let's continue to manage our finances wisely, Cheers! 🙌")

if __name__ == "__main__":
    main()
