import pandas as pd
import matplotlib.pyplot as plt

def exercise_0(df):
    df = pd.read_csv(df)
    return df

def exercise_1(df):
    list = df.columns.tolist()
    return list

def exercise_2(df, k):
    return df.head(k)

def exercise_3(df, k):
    return df.sample(n=k)

def exercise_4(df):
    df1 = df.type.unique().tolist()
    return df1

def exercise_5(df):
    n = 10
    list = df['nameDest'].value_counts()[:n]
    return list
def exercise_6(df):
    return df[df.isFraud == 1]

def exercise_7(df):
    return df.groupby("nameDest")["newbalanceDest"].agg("mean").sort_values(ascending=False)

def visual_1(df):
    def transaction_counts(df):
        cnt = df["type"].value_counts()
        return cnt
    
    def transaction_counts_split_by_fraud(df):
        fcnt = df.groupby("isFraud").size()
        return fcnt

    fig, axs = plt.subplots(2, figsize=(6,10))
    transaction_counts(df).plot(ax=axs[0], kind='bar')
    axs[0].set_title('Transaction Counts')
    axs[0].set_xlabel('Transaction Type')
    axs[0].set_ylabel('Count')
    
    transaction_counts_split_by_fraud(df).plot(ax=axs[1], kind='bar')
    axs[1].set_title('Transaction Counts Split by Fraud')
    axs[1].set_xlabel('Fraud')
    axs[1].set_ylabel('Count')
    
    fig.suptitle('Transaction Analysis')
    fig.tight_layout(rect=[0, 0.03, 1, 0.95])
    
    for ax in axs:
        for p in ax.patches:
            ax.annotate(str(p.get_height()), (p.get_x() * 1.005, p.get_height() * 1.005))
    
    return fig

def visual_2(df):
    def query(df):
        x_axis = df["oldbalanceOrg"]
        y_axis = df["oldbalanceDest"]
        return x_axis, y_axis
    
    x_values, y_values = query(df)
    plot = plt.scatter(x=x_values, y=y_values)
    
    plt.title('Balance Transfer Analysis')
    plt.xlabel('New Balance Origin')
    plt.ylabel('New Balance Destination')
    plt.xlim(left=-1e3, right=1e3)
    plt.ylim(bottom=-1e3, top=1e3)
    
    return plot


def exercise_custom(df):#percentage of frauds
    counts = df.isFraud.value_counts()     
    total = counts.iloc[0] + counts.iloc[1]     
    fraud = counts.iloc[1]     
    percentage = (fraud/total) * 100     
    return percentage
    
def visual_custom(df):#frauds according to types of transactions
    fraud_counts = df.groupby('type')['isFraud'].sum()
    plt.bar(fraud_counts.index, fraud_counts)
    plt.xlabel('Type')
    plt.ylabel('Number of Fraud Occurrences')
    plt.title('Fraud Occurrences by Type')
    x = plt.show()
    return x
