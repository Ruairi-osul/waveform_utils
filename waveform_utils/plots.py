import pandas as pd
import matplotlib.pyplot as plt


def plot_waveform_peaks(
    df_waveforms: pd.core.frame.DataFrame,
    df_peaks: pd.core.frame.DataFrame,
    neuron_id: str,
    ax=None,
    figsize: tuple = (6, 6),
    df_waveforms_neuron_col: str = "neuron_id",
    df_waveforms_value_col: str = "waveform_value",
    df_waveforms_index_col: str = "waveform_index",
    df_peaks_neuron_id_col: str = "neuron_id",
    df_peaks_peak_idx_col: str = "peak_idx",
    df_peaks_peak_value_col: str = "peak_value",
    waveform_plot_kwargs: dict = None,
    peaks_plot_kwargs: dict = None,
):
    """
    Plots an average waveform and with peaks highlighted.
    Requires two dataframes in long format: one containing waveform timepoints,
    another containing waveform peaks.

    params:
        df_waveforms: dataframe containing waveform information
        df_peaks: dataframe containing peak information
        neuron_id: id of neuron to plot
        ax: matplotlib axes object to plot on
        figsize: tuple of figure size
        df_waveforms_neuron_col: label of column containing in df_waveforms containing neuron infomation
        df_waveforms_value_col: label of column containing in df_waveforms containing waveform value infomation
        df_waveforms_index_col: label of column containing in df_waveforms containing wavefrom index infomation
        df_peaks_neuron_id_col: label of column containing in df_peaks containing neuron infomation
        df_peaks_peak_idx_col: label of column containing in df_peaks containing peak index infomation
        df_peaks_peak_value_col: label of column containing in df_peaks containing peak value infomation
        waveform_plot_kwargs: kwargs to pass to matplotlib.pyplot.plot
        peaks_plot_kwargs: kwargs to pass to matplotlib.pyplot.plot
    returns:
        axes object
    """
    if waveform_plot_kwargs is None:
        waveform_plot_kwargs = {}

    if peaks_plot_kwargs is None:
        peaks_plot_kwargs = {}

    peaks_plot_defaults = {"color": "red", "s": 140, "alpha": 1}
    waveform_plot_defaults = {"color": "black", "linewidth": 2.5, "alpha": 0.85}

    for k, v in peaks_plot_defaults.items():
        if k not in peaks_plot_kwargs:
            peaks_plot_kwargs[k] = v

    for k, v in waveform_plot_defaults.items():
        if k not in waveform_plot_kwargs:
            waveform_plot_kwargs[k] = v

    if ax is None:
        _, ax = plt.subplots(1, 1, figsize=figsize)

    ax = df_waveforms[df_waveforms[df_waveforms_neuron_col] == neuron_id].plot(
        x=df_waveforms_index_col,
        y=df_waveforms_value_col,
        **waveform_plot_kwargs,
        ax=ax
    )

    ax = df_peaks[df_peaks["neuron_id"] == neuron_id].plot(
        x=df_peaks_peak_idx_col,
        y=df_peaks_peak_value_col,
        ax=ax,
        kind="scatter",
        **peaks_plot_kwargs
    )
    ax.set_xlabel("Time [Samples]")
    ax.set_ylabel("Voltage")
    return ax
