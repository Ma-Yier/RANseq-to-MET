import pandas as pd

def main(temp="37"):
#temp = "37"  # or 44
    file_dele = temp + " delta-ldha TPM_Matrix_ann.txt"
    file_wild = temp + " wild type TPM_Matrix_ann.txt"

    # read file
    df_dele = pd.read_csv(file_dele, sep="\t")
    df_wild = pd.read_csv(file_wild, sep="\t")

    increase = []
    decrease = []
    epsilon = 1e-12

    for i in range(1, len(df_dele)):
        if df_dele.iloc[i]["gene_sym"] != df_wild.iloc[i]["gene_sym"]:
            continue
        else:
            gene_name = df_dele.iloc[i]["gene_sym"]
        dele_1 = float(df_dele.iloc[i, 15])
        dele_2 = float(df_dele.iloc[i, 16])
        wild_1 = float(df_wild.iloc[i, 15])
        wild_2 = float(df_wild.iloc[i, 16])

        if dele_1/(wild_1 + epsilon) > 1.5 and dele_2/(wild_2 + epsilon) > 1.5:
            increase.append(gene_name)

        if wild_1/(dele_1 + epsilon) > 1.5 and wild_2/(dele_2 + epsilon) > 1.5:
            decrease.append(gene_name)
    
    with open(temp + "_increase.txt", "w", encoding="utf-8") as f:
        for j in increase:
            f.write(j + "\n")

    with open(temp + "_decrease.txt", "w", encoding="utf-8") as f:
        for j in decrease:
            f.write(j + "\n")

if __name__ == "__main__":
    main("37")
    main("44")