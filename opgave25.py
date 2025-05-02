import numpy as np
import pandas as pd

W1 = {
    'P1': {'P2', 'P3'},
    'P2': {'P3'},
    'P3': {'P1'},
    'P4': {'P5'},
    'P5': {}
}

W2 = {
    'P1': {'P2'},
    'P2': {'P3'},
    'P3': {'P1'},
    'P4': {'P5'},
    'P5': {'P6'},
    'P6': {'P4'}
}

def modified_link_matrix(web, pagelist, d=0.85, print_matrix=False):
    N = len(pagelist)
    A = np.zeros((N, N))

    page_index = {page: i for i, page in enumerate(pagelist)}

    for j, page_j in enumerate(pagelist):
        outlinks = web.get(page_j, [])
        if not outlinks:
            A[:, j] = 1 / N 
        else:
            valid_links = [link for link in outlinks if link in page_index]
            L = len(valid_links)
            if L > 0:
                for linked_page in valid_links:
                    i = page_index[linked_page]
                    A[i, j] = 1 / L
            else:
                A[:, j] = 1 / N 

    E = np.ones((N, N))
    M = d * A + (1 - d) * E / N

    if print_matrix:
        df = pd.DataFrame(M, index=pagelist, columns=pagelist)
        print("\nModified Link Matrix (d = {:.2f}):\n".format(d))
        print(np.round(df, 3))
        print("\nSøjlesummer:\n", df.sum()) 

    return M

def eigenvector_PageRank(web, d=0.85):
    # Input: web er en ordbog over websider og links.
    # d er dæmpningen
    # Output: En ordbog med de samme nøgler som web og værdierne er PageRank for nøglerne
    pagelist = list(web.keys())
    M = modified_link_matrix(web, pagelist, d)
    eigvals, eigvecs = np.linalg.eig(M)
    idx = np.argmin(np.abs(eigvals - 1))
    x = np.real(eigvecs[:, idx])
    x = x / np.sum(x)
    return {pagelist[i]: float(x[i]) for i in range(len(pagelist))}

print("PageRank Egenvektor-metode:")
print(eigenvector_PageRank(W1))
def make_web(n,k,kmin=0):

    # Input: n og k er ikke-negative heltal
    # Output: web er en dictionary med n nøgler.
    # Værdien af hver nøgle er en liste, der er en delmængde af nøglerne.
    
    assert(k < n), "k skal være mindre end n (da man ikke kan linke til sig selv)"
    assert(kmin <= k), "kmin skal være mindre end eller lig med k"
    keys = list(range(n)) # definerer n nøgler fra 0 til n-1 
    web = dict()
    
    for j in keys:
        numlinks = np.random.randint(kmin, k + 1) 
        links = list(np.random.choice([x for x in keys if x != j], size=numlinks, replace=False))
        web[j] = links 

    return web


                
import time
t = time.time()
web = make_web(5000,10,0)
eigenvector_PageRank(web)
print(time.time()-t)