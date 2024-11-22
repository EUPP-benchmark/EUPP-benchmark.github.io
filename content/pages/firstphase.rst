EUPP Benchmark first phase
==========================

:date: 2024-10-30 17:00
:summary: Benchmark first phase
:page-order: 0020

The first phase of the EUPP Benchmark took place during the first phase of the EUMETNET PP Module,
with many National Meteorological Services and academics participating.
It was centered around 2 main tasks:

* Creating a common dataset to compare postprocessing methods
* Using this dataset to perform a first *simple* benchmark with the module's participants

Along the benchmark, the module also had to organize workshops.
A first workshop was held in 2019 at `the Royal Meteorological Institute of Belgium in Brussels <https://www.meteo.be>`_, and on this occasion the
requirements for the dataset were defined.

.. figure:: /images/workshop2019.jpg
    :align: center
    :alt: The flip board at the PP Module first workshop in 2019.

    The flip board at the PP Module first workshop in 2019.

These requirements were refined over several sessions during the next year and the `base dataset <{filename}./datasets.rst#base>`_ was
then constituted. After some tests, the need for a more user friendly subset of this dataset became evident and the
`Zarr format <https://zarr.dev/>`_ was selected, leading to the creation of the `EUPPBench dataset <{filename}./datasets.rst#eupp>`_ was started.
Subsequently, the need to advertise and publish this dataset led naturally to the realization of a first benchmark,
published in `Earth System Science Data (ESSD) <https://www.earth-system-science-data.net/>`_ (see `here <https://eupp-benchmark.github.io/2023/essd-publication.html#essd-publication>`_).


.. image:: /images/ESSD.png
    :alt: A map showing EUPPBench CRPSS results for all stations over the domain and for all methods.

This publication concluded the first phase of the benchmark.


