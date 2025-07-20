from pystache import render

Name = "Rick Muller"
PageTitle = Name + " Resume"
PageSummary = """\
High impact leadership in quantum information science, artificial intelligence, and advanced computing for national security."""

NPubs = 74
HIndex = 34
HomeURL = "https://rmuller.net"
ScholarURL = "https://scholar.google.com/citations?user=8ZJY9G4AAAAJ&hl=en"
LinkedInURL = "https://in.linkedin.com/in/rick-muller-62082a"
GithubURL = "http://github.com/rpmuller"
TwitterURL = "http://twitter.com/rpmuller"


Jobs = [
    {
        "Company": "IonQ",
        "Positions": [{"Title": "VP, Quantum Computing Systems", "Span": "2025-Present"}],
        "Summary": "Leading the development of IonQ's next generation quantum computing systems to deliver the world's most powerful quantum computers for commercial applications."
    },
    {"Company": "Intelligence Advanced Research Projects Activity (IARPA)",
        "Positions": [{"Title": "Director", "Span": "2024-2025"}],
        "Summary": "Directs a large research portfolio in artificial intelligence, quantum information science, biometrics, image, text, and video recognition and processing, and related technologies to give the US Intelligence Community an overwhelming information advantage."
    },
    {"Company": "Quantum Systems Accelerator (QSA)",
        "Positions": [{"Title": "Director", "Span": "2022-2024"},
            {"Title": "Deputy Director", "Span": "2020-2022"}],
        "Summary": "Led the Quantum Systems Accelerator, one of five DOE National Quantum Initiative Science Research Centers, to catalyze national leadership in quantum information science to co-design the algorithms, quantum devices, and engineering solutions needed to deliver certified quantum advantage in Department of Energy scientific applications."
    },
    {"Company": "Sandia National Laboratories",
        "Positions": [{"Title": "Senior Manager, Quantum and Advanced Microsystems Group", "Span": "2019-2024"},
            {"Title": "Program Manager, Quantum Information Sciences", "Span": "2018"},
            {"Title": "Manager, Computational Materials Science", "Span": "2017-2018"}],
        "Summary": "Led the Quantum Information Science program at Sandia to develop quantum technologies, testbeds, and centers for national security."
    },
    {"Company": "National Strategic Computing Initiative",
        "Positions": [{"Title": "Senior Staff, Joint Program Office", "Span": "2016-2017"}],
        "Summary": "Led the NSCI Joint Program Office and coordinated USG work with DOD, DOE, NSF, OSTP, OMB, NIST, IARPA. Led workshops exploring impact of foreign HPC on national and economic security, and initiated programs developing novel hardware and software paradigms for heterogeneous computing."
    },
    {"Company": "Sandia National Laboratories",
        "Positions": [{"Title": "Distinguished Member of the Technical Staff", "Span": "2016-2017"},
            {"Title": "Principal Member of the Technical Staff", "Span": "2007-2015"},
            {"Title": "Senior Member of the Technical Staff", "Span": "2003-2007"}],
        "Summary": "Deputy director of Sandia Science and Engineering of Quantum Information Sciences Research Challenge. Deputy Project Lead and Modeling Lead, Quantum Information Science and Technology, developing silicon donor and dot qubits. PI for development of QCAD simulation tool for nano- and quantum electronic devices."
    },
    {"Company": "California Institute of Technology",
        "Positions": [{"Title": "Director, Quantum Simulations Technology", "Span": "1997-2003"}],
        "Summary": "Directed the Quantum Simulations Technology group at the Caltech Materials and Process Simulation Center, focusing on developing new methods for quantum simulations and multiscale modeling."
    },
    {"Company": "University of Southern California",
        "Positions": [{"Title": "Postdoctoral Research Associate", "Span": "1994-1997"}],
        "Summary": "Postdoctoral research on computational modeling of enzyme catalysis with Nobel Laureate Prof. Arieh Warshel"
    },
]

Schools = [
    {"Name": "California Institute of Technology", "Degree": "PhD, Chemistry, 1994", 
           "Summary": "Thesis: Development and implementation of ab initio methods for application to large molecules."},
    {"Name": "Rice University", "Degree": "BA, cum Laude, Chemistry, 1988","Summary": ""},
    {"Name": "Oriel College, University of Oxford", "Degree": "Visiting Scholar, Chemistry, 1984-1985","Summary": ""}
]

QuantumPapers = [
    {"Title": "Impact of Incorporation Kinetics on Device Fabrication with Atomic Precision",
     "Authors": "Jeffrey A. Ivie, Quinn Campbell, Justin C. Koepke, Mitchell I. Brickson, Peter A. Schultz, Richard P. Muller, Andrew M. Mounce, Daniel R. Ward, Malcom S. Carroll, Ezra Bussmann, Andrew D. Baczewski, Shashank Misra",
     "Reference": "Phys. Rev. Applied 16, 054037 (2021)",
     "URL": "https://journals.aps.org/prapplied/abstract/10.1103/PhysRevApplied.16.054037",
     "Arxiv": "2105.12074",
    },
    {"Title": "Advanced Electronic Structure Calculations for Nanoelectronics",
     "Authors": "John K. Gamble, Erik Nielsen, Andrew Baczewski, Jonathan E. Moussa, Xujiao Gao, Andrew G. Salinger, and Richard P. Muller",
     "Reference": "Springer Series in Materials Science series Computational Materials, Chemistry, and Biochemistry: From Bold Initiatives to the Last Mile (2020)",
     "URL": "https://link.springer.com/chapter/10.1007/978-3-030-18778-1_18",
     "Arxiv": "",
    },
    {"Title": "The Promise of Quantum Simulation",
     "Authors": "Richard P. Muller and Robin Blume-Kohout",
     "Reference": "ACS Nano 9, 7738 (2015)",
     "URL": "https://pubs.acs.org/doi/10.1021/acsnano.5b03650",
     "Arxiv": "1507.06035",
    },
    {"Title": "ASCR Report on Quantum Computing for Science (2015)",
     "Authors": "Alan Aspuru-Guzik, Wim van Dam, Edward Farhi, Frank Gaitan, Travis Humble, Stephen Jordan, Andrew Landahl, Peter Love, Robert Lucas, Richard Muller, John Preskill, Krysta Svore, Nathan Wiebe, and Carl Williams",
     "Reference": "",
     "URL": "https://science.osti.gov/-/media/ascr/pdf/programdocuments/docs/ASCRQuantumReport-final.pdf",
     "Arxiv": "",
    },
    {"Title": "QCAD Simulation and Optimization of Semiconductor Quantum Dots",
     "Authors": "X. Gao, E. Nielsen, R. P. Muller, R. W. Young, A. G. Salinger, N. C. Bishop, M. Lilly, M. S. Carroll",
     "Reference": "Journal of Applied Physics, 114, 164302 (2013)",
     "URL": "https://pubs.aip.org/aip/jap/article-abstract/114/16/164302/395457/Quantum-computer-aided-design-simulation-and?redirectedFrom=fulltext",
     "Arxiv": "1403.7561",
    },
    {"Title": "Coherent Electron Transport by Adiabatic Passage in an Imperfect Donor Chain",
     "Authors": "Rajib Rahman, Richard P. Muller, James E. Levy, Malcolm S. Carroll, Gerhard Klimeck, Andrew D. Greentree, Lloyd C. L. Hollenberg",
     "Reference": "Physical Review B, 82, 155315 (2010)",
     "URL": "https://journals.aps.org/prb/abstract/10.1103/PhysRevB.82.155315",
     "Arxiv": "1008.1494",
    },
]

TheoryPapers = [
    {"Title": "SymPy: Symbolic Computing in Python",
     "Authors": "Aaron Meurer et al.",
     "Reference": "PeerJ Computer Science 3:e103 (2017}",
     "URL": "https://peerj.com/articles/cs-103/",
     "Arxiv": "1502.05589",
    },
    {"Title": "U.S. Leadership in High Performance Computing",
     "Authors": "Richard P. Muller and David Mountain",
     "Reference": "A Report from the NSA-DOE Technical Meeting on High Performance Computing",
     "URL": "https://www.nitrd.gov/nitrdgroups/images/b/b4/nsa_doe_hpc_techmeetingreport.pdf",
     "Arxiv": "",
    },
    {"Title": "Optimized Effective Potential from a Correlated Wave Function: OEP-GVB",
     "Authors": "Richard P. Muller and Michael P. Desjarlais",
     "Reference": "Journal of Chemical Physics. 125, 54101 (2006)",
     "URL": "https://pubs.aip.org/aip/jcp/article-abstract/125/5/054101/908943/Optimized-effective-potential-from-a-correlated?redirectedFrom=fulltext",
     "Arxiv": "",
    },
    {"Title": "Computing Approximate Eigenpairs of Symmetric Block Tridiagonal Matrices",
     "Authors": "Wilfried Gansterer, Robert C. Ward, Richard P. Muller and William A. Goddard, III",
     "Reference": "SIAM Journal on Scientific Computing, 25, 65 (2003)",
     "URL": "https://epubs.siam.org/doi/10.1137/S1064827501399432",
     "Arxiv": "",
    },
    {"Title": "Ab Initio Calculations of Free Energy Barriers for Chemical Reactions in Solution",
     "Authors": "Richard P. Muller and Arieh Warshel",
     "Reference": "Journal of Physical Chemistry, 99 (49), 17516 (1995)",
     "URL": "https://pubs.acs.org/doi/10.1021/j100049a009",
     "Arxiv": "",
    },
]

MaterialsPapers = [
    {"Title": "Influence of overcharge and over-discharge on the impedance response of LiCoO2|C batteries",
     "Authors": "Salim Erol, Mark E. Orazem and Richard P. Muller",
     "Reference": "Journal of Power Sources, 270, 92 (2014)",
     "URL": "https://iopscience.iop.org/article/10.1149/MA2011-02/17/1469",
     "Arxiv": "",
    },
    {"Title": "Simulation of Abuse Behavior of Lithium-Ion Batteries",
     "Authors": "Robert Spotnitz and Richard P. Muller",
     "Reference": "The Electrochemical Society Interface, 21, 54 (2012)",
     "URL": "https://www.electrochem.org/dl/interface/sum/sum12/sum12_p057_060.pdf",
     "Arxiv": "",
    },
    {"Title": "Meccano on the Nanoscale: A Blueprint for Making the World's Smallest Devices",
     "Authors": "Amar H. Flood, Robert J. A. Ramirez, Wei-Qiao Deng, Richard P. Muller, William A. Goddard, III and J. Frasier Stoddard",
     "Reference": "Australian Journal of Chemistry, 57, 301 (2004)",
     "URL": "https://www.publish.csiro.au/CH/CH03307",
     "Arxiv": "",
    },
    {"Title": "Quantum Mechanical-Rapid Prototyping Applied to Methane Activation",
     "Authors": "Richard P. Muller, Dean M. Philipp and William A. Goddard, III",
     "Reference": "Topics in Catalysis, 23, 81 (2003)",
     "URL": "https://link.springer.com/article/10.1023/A:1024872320512",
     "Arxiv": "",
    },
]

for template in ["template.html", 
                 "template.sidebar.html",
                 "template.right.sidebar.html",
                 "template.md"
                 ]:
    fname = template.replace("template", "rpmuller")
    open(fname, "w").write(render(open(template).read(),locals()))
