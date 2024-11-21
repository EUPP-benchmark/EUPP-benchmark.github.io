Datasets description
====================

:date: 2024-10-31 16:00
:summary: Postprocessing explained
:page-order: 0910

The EUPP Benchmark is relying on forecast datasets to compare different postprocessing methods, but at the start of the
project, not many available datasets were fit for this kind of activity.  Indeed, the training and verification of postprocessing
algorithms require pairs of forecasts and observations to be matched, both in space and time.
Therefore, the activities of the Benchmark started with the development of specific datasets.

Currently there are 2 different datasets:

1. `The base dataset <base_>`_
2. `The EUPPBench dataset <eupp_>`_

Base dataset
------------

.. _base:

The base dataset was the first to be constructed, to cover a large portion of the European domain
with `IFS <https://www.ecmwf.int/en/forecasts/documentation-and-support/changes-ecmwf-model>`_ forecasts and
`ERA5 gridded reanalysis <https://www.ecmwf.int/en/forecasts/dataset/ecmwf-reanalysis-v5>`_ (used as gridded observations).
This dataset is not used anymore directly during the benchmarking activities, but is still available online.

Data from the base dataset can only be downloaded from our `climetlab plugin <https://github.com/EUPP-benchmark/climetlab-eumetnet-postprocessing-benchmark>`_,
with the particularity that only one forecast date can be downloaded at any given time (no parallel download).

Some specification of the dataset:

* The gridded main Eumetnet postprocessing benchmark dataset contains `ECMWF <https://www.ecmwf.int>`_ ensemble and deterministic forecasts over a
  large portion of Europe, from 36 to 67° in latitude and from -6 to 17° of longitude, and covers the years 2017-2018.
* It also contains the corresponding ERA5 reanalysis for the purpose of providing observations for the benchmark.
* For some dates, it contains also `reforecasts <https://confluence.ecmwf.int/display/S2S/A+brief+description+of+reforecasts>`_  that covers
  20 years of past forecasts recomputed with the most recent model version.
* Forecasts and reforecasts lead time extent of 10 days.
* All the forecasts and reforecasts provided are the noon ECMWF runs.
* The ensemble forecasts and reforecasts also contain by default the control run (the 0-th member).
* The gridded data resolution is 0.25° x 0.25° which corresponds roughly to 25 kilometers.

.. figure:: /images/base_domain.jpg
    :align: center
    :alt: The global EUMETNET postprocessing benchmark domain.

    The global EUMETNET postprocessing benchmark domain.

.. _base_doc: https://eupp-benchmark.github.io/EUPPBench-doc/files/base_datasets.html
.. |base_doc| replace:: **https://eupp-benchmark.github.io/EUPPBench-doc/files/base_datasets.html**

**Dataset documentation:** |base_doc|_

EUPPBench dataset
-----------------

.. _eupp:

The EUPPBench dataset was designed out of `the base dataset <base_>`_ forecasts, reforecasts and gridded observations on a smaller domain and a shorter
leadtime extent of 5 days, and stored in the `Zarr format <https://zarr.dev/>`_. Stations observation data from different meteorological centers were also added.
This dataset was thus intended to provide a user-friendly, analysis-ready dataset that can be easily manipulated and processed.
The dataset was published in `Earth System Science Data (ESSD) <https://www.earth-system-science-data.net/>`_ (see `here <https://eupp-benchmark.github.io/2023/essd-publication.html#essd-publication>`_ our
news publication about this).

Like the base dataset, data from the EUPPBench dataset can be downloaded from our python `climetlab plugin <https://github.com/EUPP-benchmark/climetlab-eumetnet-postprocessing-benchmark>`_,
but it is possible to access the Zarr archive with tools from other computing languages (e.g. R or Julia). See the ESSD publication above for more details about how to use the dataset with other languages.

Some specification of the dataset:

For the gridded data
~~~~~~~~~~~~~~~~~~~~

* The gridded EUPPBench postprocessing benchmark dataset contains `ECMWF <https://www.ecmwf.int>`_ ensemble and deterministic forecasts over a small domain in Europe, from 45.75° to 53.5° in latitude,
  and from 2.5° to 10.5° in longitude, and covers the years 2017-2018.
* It also contains the corresponding ERA5 reanalysis for the purpose of providing observations for the benchmark.
* For some dates, it contains also `reforecasts <https://confluence.ecmwf.int/display/S2S/A+brief+description+of+reforecasts>`_ that covers 20 years of past forecasts recomputed with the
  most recent model version at the given date.
* Forecasts and reforecasts lead time extent of 5 days.
* All the forecasts and reforecasts provided are the noon ECMWF runs.
* The ensemble forecasts and reforecasts also contain by default the control run (the 0-th member).
* The gridded data resolution is 0.25° x 0.25° which corresponds roughly to 25 kilometers.
* Forecasts and reforecasts are 6-hourly, and include the analysis at 00Z.

For the stations data
~~~~~~~~~~~~~~~~~~~~~

* The stations EUPPBench postprocessing benchmark dataset contains ECMWF ensemble and deterministic forecasts at the grid point closest to the station locations, and covers the years 2017-2018.
* Forecasts and reforecasts lead time extent of 5 days.
* It also contains the corresponding stations observations for some important variables.
* For some dates, it contains also reforecasts that covers 20 years of past forecasts recomputed with the most recent model version at the given date.
* All the forecasts and reforecasts provided are the noon ECMWF runs.
* The ensemble forecasts and reforecasts also contain by default the control run (the 0-th member).
* 5 countries are presently available: Belgium, Austria, France, Germany, The Netherlands.

.. figure:: /images/EUPP_domain.png
    :align: center
    :alt: The domain and weather stations of the EUPPBench dataset.

    The domain and weather stations of the EUPPBench dataset.


.. _eupp_doc: https://eupp-benchmark.github.io/EUPPBench-doc/files/EUPPBench_datasets.html
.. |eupp_doc| replace:: **https://eupp-benchmark.github.io/EUPPBench-doc/files/EUPPBench_datasets.html**

**Dataset documentation:** |eupp_doc|_
