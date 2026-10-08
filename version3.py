from data import get_data
from features import add_features
from strategy import apply_strategy
from performance import evaluate
from ml_model import run_model
def main():

    running = True

    while running:

        print("\n==============================")
        print("      QUANT TERMINAL")
        print("==============================")
        print("1. Run Strategy Backtest")
        print("2. Run ML Model")
        print("3. comapare")
        print("4. Exit")
        print("==============================")

        choice = input("Enter choice: ")

     

           


     

        # STRATEGY
        if choice == "1":
            ticker = input("Enter stock ticker: ").upper()

            df = get_data(ticker)
            df = add_features(df)
            df = apply_strategy(df)
            evaluate(df)

        # ML MODEL
        elif choice == "2":
            ticker = input("Enter stock ticker: ").upper()
            
            df = get_data(ticker)
            df = add_features(df)
            accuracy,signal = run_model(df)
            print("\n--- ML RESULTS ---")
            print("Model Accuracy:", accuracy)
            print("Next day Prediction", signal)


        elif choice =="3":
             multiticker = input("how amny stocks would you like to comapare")
        

        
        
        
        
        # EXIT
        elif choice == "4":

            running = False
            print("Exiting terminal...")

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()