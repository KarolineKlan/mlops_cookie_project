import mlops_cookie_project1.data as data
import mlops_cookie_project1.evaluate as evaluate
import mlops_cookie_project1.train as train
import mlops_cookie_project1.visualize as visualize


def main():
    # Run them in the correct order
    data.preprocess_data("data/raw", "data/processed")
    print("Data preprocessed")

    train.train()
    print("Model trained")

    evaluate.evaluate("models/model.pth")
    print("Model evaluated")

    visualize.visualize("models/model.pth")
    print("Model visualized")


if __name__ == "__main__":
    main()
