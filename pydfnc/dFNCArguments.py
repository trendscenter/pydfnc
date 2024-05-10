import argparse

class dFNCOptions:
    OPTIONS = dict(
        preprocessing=dict(
        tc_detrend=dict(
            default=0,
            type=int,
            values=[0, 1, 2, 3],
            label="Detrend number",
        ),
        tc_despike=dict(
            default=False,
            type=bool,
            label="Despike timecourse"
        ),
        tc_filter=dict(
            default=0.15,
            type=float,
            min=0,
            max=1,
            label="Filter cutoff (Hz)"
        ),
        tc_covariates=dict(
            default=None,
            type=str,
            label="Regression covariates"
        ),),
        dfnc=dict(
            method_type=dict(
                default="none",
                values=["correlation",
                "l1",
                "trajectory",
                "nmi"], 
                label="Method type",
                type=str
            ),
            window_size=dict(
                default=30,
                type=float
            ),
            window_type=dict(
                default="tukey",
                values=["tukey", "gaussian"]
            ),
            window_alpha=dict(
                default=3,
                type=float
            ),
            num_l1_repetitions=dict(
                default=10,
                type=int
            )
        ),
        postprocess=dict(
            clustering_algorithm=dict(
                default="kmeans",                
                values=[
                        # sklearn
                        "kmeans", 
                        "kmedians",
                        "affinity", 
                        "meanshift", 
                        "spectral", 
                        "ward", 
                        "agglomerative", 
                        "dbscan", 
                        "hdbscan", 
                        "optics", 
                        "birch", 
                        "gmm", 
                        "bikmeans",
                        # pyclustering
                        "bang",
                        "bsas",
                        "clarans",
                        "clique",
                        "cure",
                        "dbscan",
                        "elbow",
                        "ema",
                        "fcm",
                        "gmeans",
                        "hsyncnet",
                        "kmedoids",
                        "mbsas",
                        "rock",
                        "somsc",
                        "syncnet",
                        "syncsom",
                        "ttsas",
                        "xmeans",
                        # pyclustering - neural
                        "hhn",
                        "fsync",
                        "hysteresis",
                        "legion",
                        "pcnn",
                        "som",
                        "sync",
                        "syncpr",
                        "syncsegm",
                        # deep learning methods # https://github.com/zhoushengisnoob/DeepClustering
                        "dcdc",
                        "unmix",
                        "dcc",
                        "cpac",
                        "gmvae",
                        "deepdpm",
                        "edesc",
                        "knn"
                        ]
            ),
            num_clusters=dict(
                default=6
            ),
            distance_metric=dict(
                default=city,
            )
        )
    )