from pystache import render

Name = "Rick Muller"
PageTitle = Name + " Resume"
PageSummary = """\
Director of the Intelligence Advance Research Projects Activity,
where we develop high-risk, high-payoff capabilities for the US Intelligence
Community."""

NPubs = 74
HIndex = 34
HomeURL = "https://rmuller.net"
ScholarURL = "https://scholar.google.com/citations?user=8ZJY9G4AAAAJ&hl=en"
LinkedInURL = "https://in.linkedin.com/in/rick-muller-62082a"
GithubURL = "http://github.com/rpmuller"
TwitterURL = "http://twitter.com/rpmuller"

output_fname = "rpmuller.html"
template_fname = "template.html"

Jobs = [
    {"Company": "Intelligence Advanced Research Projects Activity (IARPA)",
        "Positions": [{"Title": "Director", "Span": "2024-Present"}],
        "Summary": "Directs a large research portfolio in artificial intelligence, quantum information science, biometrics, image, text, and video recognition and processing, and related technologies to give the US Intelligence Community an overwhelming information advantage."
    },
    {"Company": "Quantum Systems Accelerator (QSA)",
        "Positions": [{"Title": "Director", "Span": "2022-2024"},
            {"Title": "Deputy Director", "Span": "2020-2022"}],
        "Summary": "The Quantum Systems Accelerator is one of five DOE National Quantum Initiative Science Research Centers that aims to catalyze national leadership in quantum information science to co-design the algorithms, quantum devices, and engineering solutions needed to deliver certified quantum advantage in Department of Energy scientific applications. The center a partnership between Lawrence Berkeley National Laboratory and Sandia National Laboratories."
    },
    {"Company": "Sandia National Laboratories",
        "Positions": [{"Title": "Senior Manager, Quantum and Advanced Microsystems Group", "Span": "2019-2024"},
            {"Title": "Program Manager, Quantum Information Sciences", "Span": "2018"},
            {"Title": "Manager, Computational Materials Science", "Span": "2017-2018"}],
        "Summary": "Led the quantum information science program at Sandia where we worked with a number of government agencies to develop quantum research centers and demonstration testbeds."
    },
    {"Company": "National Strategic Computing Initiative",
        "Positions": [{"Title": "Senior Staff, Joint Program Office", "Span": "2016-2017"}],
        "Summary": "The Joint Program Office coordinated USG work on the NSCI with DOD, DOE, NSF, OSTP, OMB, NIST, IARPA. Led workshops exploring impact of foreign HPC on national and economic security, and initiated programs developing novel hardware and software paradigms for heterogeneous computing."
    },
    {"Company": "Sandia National Laboratories",
        "Positions": [{"Title": "Distinguished Member of the Technical Staff", "Span": "2016-2017"},
            {"Title": "Principal Member of the Technical Staff", "Span": "2007-2015"},
            {"Title": "Senior Member of the Technical Staff", "Span": "2003-2007"}],
        "Summary": "Deputy director of Sandia Science and Engineering of Quantum Information Sciences Research Challenge. Deputy Project Lead and Modeling Lead, Quantum Information Science and Technology, developing Silicon donor and dot qubits. PI for development of QCAD simulation tool for nano- and quantum electronic devices. Sandia representative for quantum computing road mapping with DOE/ASCR, DOE/ASC and DOE/Materials. Modeling Team Lead, QIST GC-LDRD project developing semiconductor qubits."
    },
    {"Company": "California Institute of Technology",
        "Positions": [{"Title": "Director, Quantum Simulations Technology", "Span": "1997-2003"}],
        "Summary": "Directed the Quantum Simulations Technology group at the Caltech Materials and Process Simulation Center, focusing on developing new methods for quantum simulations and quantum computing."
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
    {"Title": "Advanced Electronic Structure Calculations for Nanoelectronics",
     "Authors": "John K. Gamble, Erik Nielsen, Andrew Baczewski, Jonathan E. Moussa, Xujiao Gao, Andrew G. Salinger, and Richard P. Muller",
     "Reference": "Springer Series in Materials Science series Computational Materials, Chemistry, and Biochemistry: From Bold Initiatives to the Last Mile (2020)",
     "URL": "",
     "Arxiv": "",
    },
    {"Title": "The Promise of Quantum Simulation",
     "Authors": "Richard P. Muller and Robin Blume-Kohout",
     "Reference": "ACS Nano 9, 7738 (2015)",
     "URL": "",
     "Arxiv": "1507.06035",
    },
    {"Title": "ASCR Report on Quantum Computing for Science (2015)",
     "Authors": "Alan Aspuru-Guzik, Wim van Dam, Edward Farhi, Frank Gaitan, Travis Humble, Stephen Jordan, Andrew Landahl, Peter Love, Robert Lucas, Richard Muller, John Preskill, Krysta Svore, Nathan Wiebe, and Carl Williams",
     "Reference": "",
     "URL": "",
     "Arxiv": "",
    },
    {"Title": "QCAD Simulation and Optimization of Semiconductor Quantum Dots",
     "Authors": "X. Gao, E. Nielsen, R. P. Muller, R. W. Young, A. G. Salinger, N. C. Bishop, M. Lilly, M. S. Carroll",
     "Reference": "Journal of Applied Physics, 114, 164302 (2013)",
     "URL": "",
     "Arxiv": "1403.7561",
    },
    {"Title": "Coherent Electron Transport by Adiabatic Passage in an Imperfect Donor Chain",
     "Authors": "Rajib Rahman, Richard P. Muller, James E. Levy, Malcolm S. Carroll, Gerhard Klimeck, Andrew D. Greentree, Lloyd C. L. Hollenberg",
     "Reference": "Physical Review B, 82, 155315 (2010)",
     "URL": "",
     "Arxiv": "1008.1494",
    },
]

TheoryPapers = [
    {"Title": "SymPy: Symbolic Computing in Python",
     "Authors": "Aaron Meurer et al.",
     "Reference": "PeerJ Computer Science 3:e103 (2017}",
     "URL": "",
     "Arxiv": "1502.05589",
    },
    {"Title": "U.S. Leadership in High Performance Computing: A Report from the NSA-DOE Technical Meeting on High Performance Computing",
     "Authors": "Richard P. Muller and David Mountain",
     "Reference": "",
     "URL": "",
     "Arxiv": "",
    },
    {"Title": "Optimized Effective Potential from a Correlated Wave Function: OEP-GVB",
     "Authors": "Richard P. Muller and Michael P. Desjarlais",
     "Reference": "Journal of Chemical Physics. 125, 54101 (2006)",
     "URL": "",
     "Arxiv": "",
    },
    {"Title": "Computing Approximate Eigenpairs of Symmetric Block Tridiagonal Matrices",
     "Authors": "Wilfried Gansterer, Robert C. Ward, Richard P. Muller and William A. Goddard, III",
     "Reference": "SIAM Journal on Scientific Computing, 25, 65 (2003)",
     "URL": "",
     "Arxiv": "",
    },
    {"Title": "Ab Initio Calculations of Free Energy Barriers for Chemical Reactions in Solution",
     "Authors": "Richard P. Muller and Arieh Warshel",
     "Reference": "Journal of Physical Chemistry, 99 (49), 17516 (1995)",
     "URL": "",
     "Arxiv": "",
    },
]

MaterialsPapers = [
    {"Title": "Influence of overcharge and over-discharge on the impedance response of LiCoO2|C batteries",
     "Authors": "Salim Erol, Mark E. Orazem and Richard P. Muller",
     "Reference": "Journal of Power Sources, 270, 92 (2014)",
     "URL": "",
     "Arxiv": "",
    },
    {"Title": "Simulation of Abuse Behavior of Lithium-Ion Batteries",
     "Authors": "Robert Spotnitz and Richard P. Muller",
     "Reference": "The Electrochemical Society Interface, 21, 54 (2012)",
     "URL": "",
     "Arxiv": "",
    },
    {"Title": "Meccano on the Nanoscale: A Blueprint for Making the World's Smallest Devices",
     "Authors": "Amar H. Flood, Robert J. A. Ramirez, Wei-Qiao Deng, Richard P. Muller, William A. Goddard, III and J. Frasier Stoddard",
     "Reference": "Australian Journal of Chemistry, 57, 301 (2004)",
     "URL": "",
     "Arxiv": "",
    },
    {"Title": "Quantum Mechanical-Rapid Prototyping Applied to Methane Activation",
     "Authors": "Richard P. Muller, Dean M. Philipp and William A. Goddard, III",
     "Reference": "Topics in Catalysis, 23, 81 (2003)",
     "URL": "",
     "Arxiv": "",
    },
]
template = open(template_fname).read()
print(template)
open(output_fname, "w").write(render(template, locals()))