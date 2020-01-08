===========================================================================
Moving Your Experimentation Project to Production Applications with Pyspark
===========================================================================

:date: 2020-01-06 21:09
:url: talk/moving.html
:save_as: talk/moving.html

Moving Your Experimentation Project to Production Applications with Pyspark
===========================================================================

Struggling to bring data science projects from lab to production?  Especially
from small to large scale of data, you may learn something from this talk about
some procedures we learned for designing production-ready spark jobs with
Pyspark and challenges faced along the way.

Talk Description
================

A huge number of machine learning projects starts to yield promising results
from proof of concept stage.  However, data scientists usually have confusion
about how to integrate resulting models into existing systems and processes if
without software or machine learning engineering experience.  Especially, when
data throughput in production becomes significantly larger than laboratory
scales, data processing and modeling need to be deployed in distributed
systems.

With its in-memory processing capabilities, Apache Spark has been all the rage
for large scale data processing and analytics.  Adopting Apache Spark in
production become common.  High-level APIs also make the learning cure of
Apache Spark flatter.

However, it is still not painless to move experimenting Python scripts into
Apache Spark jobs in production.  Our talk aims to relieve the pain by sharing
the procedures we learned for designing production-ready spark jobs with
Pyspark.  We will start by briefly introducing Apache Spark.  The main focus
will about how to prepare your code for production with Pyspark, including
comparing the difference between Apache Dataframe and Pandas Dataframe.  Then,
through a few examples, we will demonstrate how to deploy machine learning
models with Pyspark.

Speaker
=======

`Shuhsi Lin <https://medium.com/@suci>`__ is working in a data team, focuses on
stream processing and IoT applications.  He is passionate about data
storytelling with data visualization and building an engineering culture.

Daren Hsu is a data Engineer who focuses on data ingestion in Hadoop ecosystem.
He loves to technical books and try new technologies.  His primary area of
research during my graduate studies is optimization theory and scheduling.
