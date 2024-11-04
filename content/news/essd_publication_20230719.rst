Publication of the new EUMETNET postprocessing benchmark dataset in ESSD !
==========================================================================

:date: 2023-07-19 11:20
:author: Jonathan Demaeyer
:summary: The EUMETNET postprocessing (PP) module has just published its first dataset paper to date in Earth System Science Data (ESSD).
:slug: essd-publication
:tags: dataset, benchmark
:category: dataset

.. image:: /images/ESSD.png
    :alt: A map showing EUPPBench CRPSS results for all stations over the domain and for all methods.

The EUMETNET postprocessing (PP) module has just published its first dataset paper to date in `Earth System Science Data <https://www.earth-system-science-data.net/>`_.

This paper is about EUPPBench, the first version of an open postprocessing benchmark dataset which can be used in many different ways by the scientific community
to benchmark new and old postprocessing methods. This dataset and the description article are the result of the hard work of the many module participants.

The dataset includes both gridded and station-point ECMWF forecasts along with the observations, time-paired together to obtain an 'analysis-ready dataset' that
can be used directly by the statistical and machine learning community.

.. figure:: /images/precip.png
    :align: center
    :alt: A gridded forecast of the total precipitation at various lead time issued on the 13 January 2017, and its ERA5 observation fields, both part of the gridded dataset.

    A gridded forecast of the total precipitation at various lead time issued on the 13 January 2017, and its ERA5 observation fields, both part of the gridded dataset.

Many past forecasts (reforecasts) are also included to enable training of postprocessing algorithm, representing 20 years of data.

.. figure:: /images/precip_reforecast.png
    :align: center
    :alt: A gridded reforecast of the total precipitation at various lead time issued on the 13 January 1997, and its ERA5 observation fields, both part of the gridded dataset.

    A gridded reforecast of the total precipitation at various lead time issued on the 13 January 1997, and its ERA5 observation fields, both part of the gridded dataset.

The gridded observations corresponding to the gridded forecasts have been obtained by using the ERA5 reanalysis data (see https://climate.copernicus.eu/climate-reanalysis)
and cover a portion of central Europe. The station data include forecasts and observations of 100+ stations inside this domain.

.. figure:: /images/EUPP_domain.png
    :align: center
    :alt: The domain and weather stations of the EUPPBench dataset.

    The domain and weather stations of the EUPPBench dataset.

On the practical side, the recommended way to download the data is through a ECMWF climetlab plugin (available at  https://github.com/EUPP-benchmark/climetlab-eumetnet-postprocessing-benchmark),
returning xarray datasets which can then be used directly or converted to netCDF files. But other ways are possible, see the Supplementary Information in the paper.

The data are stored on the ECMWF European Weather Cloud (EWC). Many thanks to them for their support.

Many more scientific activities will be organized in the future around this dataset, so stay tuned if you are interested !
Our wish with the PP module participants is that this first step will foster many interesting developments in the field of postprocessing
and verification of weather forecasts in the future.

.. _essd_link: https://essd.copernicus.org/articles/15/2635/2023/
.. |essd_link| replace:: **https://essd.copernicus.org/articles/15/2635/2023/**

**See** |essd_link|_ **for the full article !**
