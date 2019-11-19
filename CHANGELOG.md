# Change Log

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/) and this project adheres to [Semantic Versioning](http://semver.org/).

## [0.1.0](https://github.com/Esukhia/bordr/releases/tag/v0.1.0) - 20191119
### Removed
 * all language data
 * all `InitialTagger`s except for a generic one adapted to Tibetan
 * ExtRDRPOSTagger is removed because it won't be use in the foreseeable future
### Changed
 * `InitialTagger` becomes `InitialTagger4Bo` and incorporates support of syllable-suffixes
 * all encodings turned from `utf-8` to `utf-8-sig`
 * all `print` messages are boxed into logs or msgs that are returned by the methods/functions
 * absolute imports are turned into relative imports (that hack is not needed anymore for pypi packages)
 * `RDRPOSTagger/run()` becomes `rdr()` and all CLI arguments/options are turned into arguments of `rdr()`
 * temporary files used by RDRPOSTagger are not deleted at `train` time.
 * `black` is run on the whole codebase.
### Added
 * `evaluate()` function added to `Utility/Eval.py` and depending on the presence/absence of the `fullDictFile` arg,
    it runs either `computeAccuracies()` or `computeAccuracy()`
 * interface into RDRPOSTagger: `rdr()`, `evaluate()`, `NUMBER_OF_PROCESSES` and `THRESHOLD` are exposed
    on the root level of bordr. the two constants to configure RDRPOSTagger, `rdr()` to train and tag data,
    `evaluate()` to check the performance of the trained model.
