# Neural Poet

[![License][license badge]][license]

![Story][story]

The whole approach contains 4 components:

-   skip-thought vectors
-   image-sentence embeddings
-   conditional neural language models
-   style shifting

The 'style-shifting' operation is what allows our model to transfer standard image captions to the style of stories from novels. The only source of supervision in our models is from [Microsoft COCO](http://mscoco.org/) captions.

That is, we did not collect any new training data to directly predict stories given images.

# Quickstart

## Clone Repository

```sh
$ git clone https://github.com/jjangsangy/neuralpoet.git
```

## Create a virtualenv

```sh
$ virtualenv -p python3 venv
```

## Source Virtualenv

    $ source venv/bin/activate

## Install Python Dependencies

```sh
$ pip install --upgrade pip setuptools wheel
$ pip install -r requirements.txt
```

## Run Server

    $ python manage.py runserver
    * Running on http://127.0.0.1:8080/ (Press CTRL+C to quit)

# References

Ryan Kiros, Yukun Zhu, Ruslan Salakhutdinov, Richard S. Zemel, Antonio Torralba, Raquel Urtasun, and Sanja Fidler. **"Skip-Thought Vectors."** _arXiv preprint arXiv:1506.06726 (2015)._

    @article{kiros2015skip,
      title={Skip-Thought Vectors},
      author={Kiros, Ryan and Zhu, Yukun and Salakhutdinov, Ruslan and Zemel, Richard S and Torralba, Antonio and Urtasun, Raquel and Fidler, Sanja},
      journal={arXiv preprint arXiv:1506.06726},
      year={2015}
    }

Samuel R. Bowman, Luke Vilnis, Oriol Vinyals, Andrew M. Dai, Rafal J{'{o}}zefowicz Samy Bengio.
**Generating Sentences from a Continuous Space** _<http://arxiv.org/abs/1511.06349>_

    @article{DBLP:journals/corr/BowmanVVDJB1
          title     = {Generating Sentences from a Continuous Space},
          journal   = {CoRR},
          year      = {2015},
          biburl    = {<http://dblp2.uni-trier.de/rec/bib/journals/corr/BowmanVVDJB15}>,
          bibsource = {dblp computer science bibliography, <http://dblp.org}>
    }

Zhang, Xingxing, and Mirella Lapata. EMNLP. 2014.
**"Chinese Poetry Generation with Recurrent Neural Networks."** <http://www.aclweb.org/old_anthology/D/D14/D14-1074.pdf>

    @inproceedings{zhang2014chinese,
      title={Chinese Poetry Generation with Recurrent Neural Networks.},
      author={Zhang, Xingxing and Lapata, Mirella},
      booktitle={EMNLP},
      pages={670--680},
      year={2014}
    }

[license]: https://raw.githubusercontent.com/jjangsangy/neuralpoet/master/LICENSE "License"

[license badge]: https://img.shields.io/pypi/l/coverage.svg "Apache 2.0 Badge"

[story]: content/man-picture-mirror.jpg

[samim]: https://medium.com/@samim/generating-stories-about-images-d163ba41e4ed

[chinese poetry]: http://www.aclweb.org/old_anthology/D/D14/D14-1074.pdf

[google]: http://arxiv.org/pdf/1511.06349.pdf
