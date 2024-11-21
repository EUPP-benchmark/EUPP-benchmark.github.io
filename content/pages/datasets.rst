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
* For some dates, it contains also reforecasts that covers 20 years of past forecasts recomputed with the most recent model version.
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

TODO

.. figure:: /images/EUPP_domain.png
    :align: center
    :alt: The domain and weather stations of the EUPPBench dataset.

    The domain and weather stations of the EUPPBench dataset.


.. _eupp_doc: https://eupp-benchmark.github.io/EUPPBench-doc/files/EUPPBench_datasets.html
.. |eupp_doc| replace:: **https://eupp-benchmark.github.io/EUPPBench-doc/files/EUPPBench_datasets.html**

**Dataset documentation:** |eupp_doc|_
