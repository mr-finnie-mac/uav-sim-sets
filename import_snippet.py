import pandas as pd
POSITION_COLS = ["x_m", "y_m", "alt_m"]


def load_flights(data_dir, signal_col):
    """ 
    read every csv in the data directory and add them together into one set
    """
    paths = sorted(glob.glob(os.path.join(data_dir, "*.csv")))
    if not paths:
        raise FileNotFoundError(f"No CSV files found in: {data_dir}")

    frames = []
    for path in paths:
        df = pd.read_csv(path)
        df["__flight__"] = os.path.basename(path)  #remember flightt layer
        frames.append(df)
    data = pd.concat(frames, ignore_index=True)

    missing = [c for c in POSITION_COLS + [signal_col] if c not in data.columns]
    if missing:
        raise ValueError(f"CSVs are missing required columns: {missing}")

    data = data.dropna(subset=POSITION_COLS + [signal_col])
    xyz = data[POSITION_COLS].to_numpy(dtype=np.float32)
    signal = data[signal_col].to_numpy(dtype=np.float32)
    flights = data["__flight__"].to_numpy()
    print(f"Loaded {len(paths)} flight file(s), {len(xyz):,} samples total.")
    return xyz, signal, flights


def validation_split(data_dir, signal_col):
    xyz, signal, flights = load_flights(args.data_dir, args.signal_col)

    # split off a validation set using xyz
    perm = rng.permutation(len(xyz))
    n_val = max(1, int(len(xyz) * args.val_frac))
    val_idx, train_idx = perm[:n_val], perm[n_val:]
    train_xyz, train_signal = xyz[train_idx], signal[train_idx]
    val_xyz, val_signal = xyz[val_idx], signal[val_idx]

return train_xyz, train_signal, val_xyz, val_signal
