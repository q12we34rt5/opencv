# -*- coding: utf-8 -*-
#
# opencvstd documentation build configuration file, created by
# sphinx-quickstart on Mon Feb 14 00:30:43 2011.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys, os, re

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.insert(0, os.path.abspath('.'))

# -- General configuration -----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['sphinx.ext.pngmath', 'sphinx.ext.ifconfig', 'sphinx.ext.todo', 'sphinx.ext.extlinks', 'ocv', 'sphinx.ext.doctest']
doctest_test_doctest_blocks = 'block'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'OpenCV'
copyright = u'2011, opencv dev team'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.

version_file = open("../modules/core/include/opencv2/core/version.hpp", "rt").read()
version_major = re.search("^W*#\W*define\W+CV_MAJOR_VERSION\W+(\d+)\W*$", version_file, re.MULTILINE).group(1)
version_minor = re.search("^W*#\W*define\W+CV_MINOR_VERSION\W+(\d+)\W*$", version_file, re.MULTILINE).group(1)
version_patch = re.search("^W*#\W*define\W+CV_SUBMINOR_VERSION\W+(\d+)\W*$", version_file, re.MULTILINE).group(1)

# The short X.Y version.
version = version_major + '.' + version_minor
# The full version, including alpha/beta/rc tags.
release = version_major + '.' + version_minor + '.' + version_patch

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['doc/tutorials/definitions']

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

todo_include_todos=True

# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'blue'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = ['_themes']

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = 'opencv-logo2.png'

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'opencv'

# OpenCV docs use some custom LaTeX macros in the formula. Make sure we include the definitions
pngmath_latex_preamble = r"""
\usepackage{euler}\usepackage[usenames,dvipsnames]{color}\usepackage{amssymb}\usepackage{amsmath}\usepackage{bbm}\usepackage{colortbl}
\newcommand{\matTT}[9]{
\[
\left|\begin{array}{ccc}
 #1 & #2 & #3\\
 #4 & #5 & #6\\
 #7 & #8 & #9
\end{array}\right|
\]
}

\newcommand{\fork}[4]{
  \left\{
  \begin{array}{l l}
  #1 & \mbox{#2}\\
  #3 & \mbox{#4}\\
  \end{array} \right.}
\newcommand{\forkthree}[6]{
  \left\{
  \begin{array}{l l}
  #1 & \mbox{#2}\\
  #3 & \mbox{#4}\\
  #5 & \mbox{#6}\\
  \end{array} \right.}

\newcommand{\vecthree}[3]{
\begin{bmatrix}
 #1\\
 #2\\
 #3
\end{bmatrix}
}

\newcommand{\vecthreethree}[9]{
\begin{bmatrix}
 #1 & #2 & #3\\
 #4 & #5 & #6\\
 #7 & #8 & #9
\end{bmatrix}
}
"""

# -- Options for LaTeX output --------------------------------------------------

# The paper size ('letter' or 'a4').
#latex_paper_size = 'letter'

# The font size ('10pt', '11pt' or '12pt').
#latex_font_size = '10pt'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
  ('modules/refman', 'opencv2refman.tex', u'The OpenCV Reference Manual',
   u'', 'manual'),
  ('doc/user_guide/user_guide', 'opencv_user.tex', u'The OpenCV User Guide',
   u'', 'manual'), 
  ('doc/tutorials/tutorials', 'opencv_tutorials.tex', u'The OpenCV Tutorials',
   u'', 'manual'), 
]

preamble ="""
\usepackage{euler}
\usepackage[scaled=0.85]{beramono}
\usepackage{mymath}\usepackage{amssymb}\usepackage{amsmath}\usepackage{bbm}\setcounter{secnumdepth}{1}
\usepackage{colortbl}
\usepackage{enumitem}
\setlist{labelsep=1ex}
"""

latex_elements = {'preamble': preamble}

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Additional stuff for the LaTeX preamble.
#latex_preamble = ''

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
latex_domain_indices = True


# -- Options for manual page output --------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'opencv', u'The OpenCV Reference Manual',
     [u'opencv-dev@itseez.com'], 1)
]

# ---- External links for tutorials -----------------
extlinks = {
            'basicstructures' : ('http://opencv.itseez.com/modules/core/doc/basic_structures.html#%s', None),
            'oldbasicstructures' : ('http://opencv.itseez.com/modules/core/doc/old_basic_structures.html#%s', None),
            'readwriteimagevideo' : ('http://opencv.itseez.com/modules/highgui/doc/reading_and_writing_images_and_video.html#%s', None),
            'operationsonarrays' : ('http://opencv.itseez.com/modules/core/doc/operations_on_arrays.html#%s', None),
            'utilitysystemfunctions':('http://opencv.itseez.com/modules/core/doc/utility_and_system_functions_and_macros.html#%s', None),
            'imgprocfilter':('http://opencv.itseez.com/modules/imgproc/doc/filtering.html#%s', None),
            'svms':('http://opencv.itseez.com/modules/ml/doc/support_vector_machines.html#%s', None),
            'drawingfunc':('http://opencv.itseez.com/modules/core/doc/drawing_functions.html#%s', None),
            'xmlymlpers':('http://opencv.itseez.com/modules/core/doc/xml_yaml_persistence.html#%s', None),
            'huivideo' : ('http://opencv.itseez.com/modules/highgui/doc/reading_and_writing_images_and_video.html#%s', None),
            'gpuinit' : ('http://opencv.itseez.com/modules/gpu/doc/initalization_and_information.html#%s', None),
            'gpudatastructure' : ('http://opencv.itseez.com/modules/gpu/doc/data_structures.html#%s', None),
            'gpuopmatrices' : ('http://opencv.itseez.com/modules/gpu/doc/operations_on_matrices.html#%s', None),
            'gpuperelement' : ('http://opencv.itseez.com/modules/gpu/doc/per_element_operations.html#%s', None),
            'gpuimgproc' : ('http://opencv.itseez.com/modules/gpu/doc/image_processing.html#%s', None),
            'gpumatrixreduct' : ('http://opencv.itseez.com/modules/gpu/doc/matrix_reductions.html#%s', None),
            'filtering':('http://opencv.itseez.com/modules/imgproc/doc/filtering.html#%s', None),
            'flann' : ('http://opencv.willowgarage.com/documentation/cpp/flann_fast_approximate_nearest_neighbor_search.html#%s', None ),
            'calib3d' : ('http://opencv.itseez.com/trunk/modules/calib3d/doc/camera_calibration_and_3d_reconstruction.html#%s', None ),
            'feature2d' : ('http://opencv.itseez.com/trunk/modules/imgproc/doc/feature_detection.html#%s', None ),
            'imgproc_geometric' : ('http://opencv.itseez.com/trunk/modules/imgproc/doc/geometric_transformations.html#%s', None ),
            
            'opencv_group' : ('http://tech.groups.yahoo.com/group/OpenCV/%s', None),

            'cvt_color': ('http://opencv.willowgarage.com/documentation/cpp/imgproc_miscellaneous_image_transformations.html#cv-cvtcolor%s', None),
            'imread':    ('http://opencv.willowgarage.com/documentation/cpp/highgui_reading_and_writing_images_and_video.html?highlight=imread#imread%s', None),
            'imwrite':   ('http://opencv.willowgarage.com/documentation/cpp/highgui_reading_and_writing_images_and_video.html?highlight=imread#cv-imwrite%s', None),
            'imshow':    ('http://opencv.willowgarage.com/documentation/cpp/highgui_user_interface.html?highlight=imshow#imshow%s', None),
            'named_window': ('http://opencv.willowgarage.com/documentation/cpp/highgui_user_interface.html?highlight=namedwindow#namedWindow%s', None),
            'wait_key': ('http://opencv.willowgarage.com/documentation/cpp/highgui_user_interface.html?highlight=namedwindow#cv-waitkey%s', None),
            'add_weighted': ('http://opencv.willowgarage.com/documentation/cpp/core_operations_on_arrays.html?highlight=addweighted#addWeighted%s', None),
            'saturate_cast': ('http://opencv.willowgarage.com/documentation/cpp/core_operations_on_arrays.html?highlight=saturate_cast#saturate_cast%s', None),
            'mat_zeros': ('http://opencv.willowgarage.com/documentation/cpp/core_basic_structures.html?highlight=zeros#Mat::zeros%s', None),
            'convert_to': ('http://opencv.willowgarage.com/documentation/cpp/core_basic_structures.html?#Mat::convertTo%s', None),
            'create_trackbar': ('http://opencv.willowgarage.com/documentation/cpp/user_interface.html%s', None),
            'point': ('http://opencv.willowgarage.com/documentation/cpp/basic_structures.html?#point%s', None),
            'scalar': ('http://opencv.willowgarage.com/documentation/cpp/core_basic_structures.html?#scalar%s', None),
            'line': ('http://opencv.willowgarage.com/documentation/cpp/core_drawing_functions.html?#cv-line%s', None),
            'ellipse': ('http://opencv.willowgarage.com/documentation/cpp/core_drawing_functions.html?#cv-ellipse%s', None),
            'rectangle': ('http://opencv.willowgarage.com/documentation/cpp/core_drawing_functions.html?#cv-rectangle%s', None),
            'circle': ('http://opencv.willowgarage.com/documentation/cpp/core_drawing_functions.html?#cv-circle%s', None),
            'fill_poly': ('http://opencv.willowgarage.com/documentation/cpp/core_drawing_functions.html?#cv-fillpoly%s', None),
            'rng': ('http://opencv.willowgarage.com/documentation/cpp/core_operations_on_arrays.html?#rng%s', None),
            'put_text': ('http://opencv.willowgarage.com/documentation/cpp/core_drawing_functions.html?#putText%s', None),
            'gaussian_blur': ('http://opencv.willowgarage.com/documentation/cpp/image_filtering.html#cv-gaussianblur%s', None),
            'blur': ('http://opencv.willowgarage.com/documentation/cpp/image_filtering.html#cv-blur%s', None),
            'median_blur': ('http://opencv.willowgarage.com/documentation/cpp/image_filtering.html#cv-medianblur%s', None), 
            'bilateral_filter': ('http://opencv.willowgarage.com/documentation/cpp/image_filtering.html#cv-bilateralfilter%s', None),
            'erode': ('http://opencv.jp/opencv-2.2_org/cpp/imgproc_image_filtering.html#cv-erode%s', None),
            'dilate': ('http://opencv.jp/opencv-2.2_org/cpp/imgproc_image_filtering.html#cv-dilate%s', None),
            'get_structuring_element': ('http://opencv.jp/opencv-2.2_org/cpp/imgproc_image_filtering.html#cv-getstructuringelement%s', None),
            'flood_fill': ( 'http://opencv.jp/opencv-2.2_org/cpp/imgproc_miscellaneous_image_transformations.html?#floodFill%s', None),
            'morphology_ex': ('http://opencv.jp/opencv-2.2_org/cpp/imgproc_image_filtering.html?highlight=morphology#morphologyEx%s', None),
            'pyr_down': ('http://opencv.willowgarage.com/documentation/cpp/imgproc_image_filtering.html#cv-pyrdown%s', None),
            'pyr_up': ('http://opencv.willowgarage.com/documentation/cpp/imgproc_image_filtering.html#cv-pyrup%s', None),
            'resize': ('http://opencv.willowgarage.com/documentation/cpp/imgproc_geometric_image_transformations.html#cv-resize%s', None),
            'threshold': ('http://opencv.willowgarage.com/documentation/cpp/miscellaneous_image_transformations.html#cv-threshold%s', None),
            'filter2d': ('http://opencv.willowgarage.com/documentation/cpp/image_filtering.html#cv-filter2d%s', None),
            'copy_make_border': ('http://opencv.willowgarage.com/documentation/cpp/imgproc_image_filtering.html?#copyMakeBorder%s', None),
            'sobel': ('http://opencv.willowgarage.com/documentation/cpp/image_filtering.html#cv-sobel%s', None),
             'scharr': ('http://opencv.willowgarage.com/documentation/cpp/image_filtering.html#cv-scharr%s', None),
            'laplacian': ('http://opencv.willowgarage.com/documentation/cpp/image_filtering.html#cv-laplacian%s', None),
            'canny': ('http://opencv.willowgarage.com/documentation/cpp/imgproc_feature_detection.html?#Canny%s', None),
            'copy_to': ('http://opencv.willowgarage.com/documentation/cpp/core_basic_structures.html?#Mat::copyTo%s', None), 	
            'hough_lines' : ('http://opencv.willowgarage.com/documentation/cpp/imgproc_feature_detection.html?#cv-houghlines%s', None),
            'hough_lines_p' : ('http://opencv.willowgarage.com/documentation/cpp/imgproc_feature_detection.html?#cv-houghlinesp%s', None),
            'hough_circles' : ('http://opencv.willowgarage.com/documentation/cpp/imgproc_feature_detection.html?#cv-houghcircles%s', None),
            'remap' : ('http://opencv.willowgarage.com/documentation/cpp/imgproc_geometric_image_transformations.html?#remap%s', None),
            'warp_affine' : ('http://opencv.willowgarage.com/documentation/cpp/imgproc_geometric_image_transformations.html?#cv-warpaffine%s' , None),
            'get_rotation_matrix_2d' : ('http://opencv.willowgarage.com/documentation/cpp/imgproc_geometric_image_transformations.html?#cv-getrotationmatrix2d%s', None),
            'get_affine_transform' : ('http://opencv.willowgarage.com/documentation/cpp/imgproc_geometric_image_transformations.html?#cv-getaffinetransform%s', None),
            'equalize_hist' : ('http://opencv.willowgarage.com/documentation/cpp/imgproc_histograms.html?#equalizeHist%s', None),
            'split' : ('http://opencv.willowgarage.com/documentation/cpp/core_operations_on_arrays.html?#split%s', None),
            'calc_hist' : ('http://opencv.willowgarage.com/documentation/cpp/imgproc_histograms.html?#calcHist%s', None),
            'normalize' : ('http://opencv.willowgarage.com/documentation/cpp/core_operations_on_arrays.html?#normalize%s', None),
            'match_template' : ('http://opencv.willowgarage.com/documentation/cpp/imgproc_object_detection.html?#matchTemplate%s', None),
            'min_max_loc' : ('http://opencv.willowgarage.com/documentation/cpp/core_operations_on_arrays.html?#minMaxLoc%s', None),
            'mix_channels' : ( 'http://opencv.willowgarage.com/documentation/cpp/core_operations_on_arrays.html?#mixChannels%s', None),
            'calc_back_project' : ('http://opencv.willowgarage.com/documentation/cpp/imgproc_histograms.html?#calcBackProject%s', None),
            'compare_hist' : ('http://opencv.willowgarage.com/documentation/cpp/imgproc_histograms.html?#compareHist%s', None),
            'corner_harris' : ('http://opencv.willowgarage.com/documentation/cpp/imgproc_feature_detection.html?#cornerHarris%s', None),
            'good_features_to_track' : ('http://opencv.willowgarage.com/documentation/cpp/imgproc_feature_detection.html?#cv-goodfeaturestotrack%s', None),
            'corner_min_eigenval' : ('http://opencv.willowgarage.com/documentation/cpp/imgproc_feature_detection.html?#cv-cornermineigenval%s', None), 
            'corner_eigenvals_and_vecs' : ('http://opencv.willowgarage.com/documentation/cpp/imgproc_feature_detection.html?#cv-cornereigenvalsandvecs%s', None), 
            'corner_sub_pix' : ('http://opencv.willowgarage.com/documentation/cpp/imgproc_feature_detection.html?#cv-cornersubpix%s', None),
            'find_contours' : ('http://opencv.willowgarage.com/documentation/cpp/imgproc_structural_analysis_and_shape_descriptors.html#cv-findcontours%s', None), 
            'convex_hull' : ('http://opencv.willowgarage.com/documentation/cpp/imgproc_structural_analysis_and_shape_descriptors.html#cv-convexhull%s', None),
            'draw_contours' : ('http://opencv.willowgarage.com/documentation/cpp/imgproc_structural_analysis_and_shape_descriptors.html#cv-drawcontours%s', None),
            'bounding_rect' : ('http://opencv.willowgarage.com/documentation/cpp/imgproc_structural_analysis_and_shape_descriptors.html#cv-boundingrect%s', None),
            'min_enclosing_circle' : ('http://opencv.willowgarage.com/documentation/cpp/imgproc_structural_analysis_and_shape_descriptors.html#cv-minenclosingcircle%s', None),
            'min_area_rect' : ('http://opencv.willowgarage.com/documentation/cpp/imgproc_structural_analysis_and_shape_descriptors.html#cv-minarearect%s', None),
            'fit_ellipse' : ('http://opencv.willowgarage.com/documentation/cpp/imgproc_structural_analysis_and_shape_descriptors.html#cv-fitellipse%s', None),
            'moments' : ('http://opencv.willowgarage.com/documentation/cpp/imgproc_structural_analysis_and_shape_descriptors.html#cv-moments%s', None),
            'contour_area' : ('http://opencv.willowgarage.com/documentation/cpp/imgproc_structural_analysis_and_shape_descriptors.html#cv-contourarea%s', None),
            'arc_length' : ('http://opencv.willowgarage.com/documentation/cpp/imgproc_structural_analysis_and_shape_descriptors.html#cv-arclength%s', None),
            'point_polygon_test' : ('http://opencv.willowgarage.com/documentation/cpp/imgproc_structural_analysis_and_shape_descriptors.html#cv-pointpolygontest%s', None),
            'feature_detector' : ( 'http://opencv.willowgarage.com/documentation/cpp/features2d_common_interfaces_of_feature_detectors.html#featuredetector%s', None),
            'feature_detector_detect' : ('http://opencv.willowgarage.com/documentation/cpp/features2d_common_interfaces_of_feature_detectors.html#cv-featuredetector-detect%s', None ),
            'surf_feature_detector' : ('http://opencv.willowgarage.com/documentation/cpp/features2d_common_interfaces_of_feature_detectors.html#surffeaturedetector%s', None ),
            'draw_keypoints' : ('http://opencv.willowgarage.com/documentation/cpp/features2d_drawing_function_of_keypoints_and_matches.html#cv-drawkeypoints%s', None ),
            'descriptor_extractor': ( 'http://opencv.willowgarage.com/documentation/cpp/features2d_common_interfaces_of_descriptor_extractors.html#descriptorextractor%s', None ),
            'descriptor_extractor_compute' : ( 'http://opencv.willowgarage.com/documentation/cpp/features2d_common_interfaces_of_descriptor_extractors.html#cv-descriptorextractor-compute%s', None ),
            'surf_descriptor_extractor' : ( 'http://opencv.willowgarage.com/documentation/cpp/features2d_common_interfaces_of_descriptor_extractors.html#surfdescriptorextractor%s', None ),
            'draw_matches' : ( 'http://opencv.willowgarage.com/documentation/cpp/features2d_drawing_function_of_keypoints_and_matches.html#cv-drawmatches%s', None ),
            'find_homography' : ('http://opencv.willowgarage.com/documentation/cpp/calib3d_camera_calibration_and_3d_reconstruction.html?#findHomography%s', None),
            'perspective_transform' : ('http://opencv.willowgarage.com/documentation/cpp/core_operations_on_arrays.html?#perspectiveTransform%s', None ),
            'flann_based_matcher' : ('http://opencv.willowgarage.com/documentation/cpp/features2d_common_interfaces_of_descriptor_matchers.html?#FlannBasedMatcher%s', None),
            'brute_force_matcher' : ('http://opencv.willowgarage.com/documentation/cpp/features2d_common_interfaces_of_descriptor_matchers.html?#BruteForceMatcher%s', None ),
            'cascade_classifier' : ('http://opencv.willowgarage.com/documentation/cpp/objdetect_cascade_classification.html#cascadeclassifier%s', None ),
            'cascade_classifier_load' : ('http://opencv.willowgarage.com/documentation/cpp/objdetect_cascade_classification.html#cv-cascadeclassifier-load%s', None ),
            'cascade_classifier_detect_multiscale' : ('http://opencv.willowgarage.com/documentation/cpp/objdetect_cascade_classification.html#cv-cascadeclassifier-detectmultiscale%s', None )	
           }