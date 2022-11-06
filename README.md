# General Notes

Over the years of becoming a Software Engineer, I have continually discovered the vast amount of knowledge that there is to obtain within the field. I have been continually writing my own personal books, where I take the time to hand write all of my notes by hand. I have found that writing down the notes by hand has led to a stronger understanding as I take the time to write them down character by character rather than typing it. When needed, I can therefore quickly find my notes and remind myself of the information quickly.

I have now written several books containing a wide variety of information and despite initially being very organized, some of the notes have become slightly disorganized and harder to find while sometimes wanting to reflect on the notes, but I may be away from home and unable to access them. I would also like to find a way to make sure I have my notes stored so I still have the information if the books were lost.

The purpose of this repository is to store my personal notes as a quick reference point to refresh my knowledge on something. I have taken notes from external resources and rewritten or restructured them in a way that I have personally found easier to understand.

## Structure
For more general note-taking, a markdown file is used, otherwise, the required Programming Language file format is used for displaying Code. The construction of diagrams is used by using the markdown extension called [Mermaid](https://mermaid-js.github.io/mermaid/#/), which is supported by Github.

Mathjax was utilized for standard mathematical equations using Github flavoured markdown, but inline vectors were shown to be not possible, instead I am writing these files using LaTeX and storing them using overleaf. To display them in Github I need to export them into pdf format and upload the file here, to finally be rendered nicely.

Unfortunately automatically regenerating pdf files for my associated LaTeX files was not possible. I use Overleaf to edit my LaTeX files and sync them to my Github account, but need to manually download and upload the pdf file. Github actions could not be utilized to automatically regenerate the pdf files to the an infinite loop occurring. This would happen when I commit and push my LaTeX file, run a Github action to regenerate the associated pdf, commit and upload this to the same repository. The Github action which then committed and pushed the new pdf file would then spawn another Github action, hence, causing an infinite loop.
