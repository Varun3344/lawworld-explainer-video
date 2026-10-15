// Usage: swift person_mask.swift in.png out_mask.png
// Writes a grayscale person mask (white = person) at the input image size, using Vision's accurate person segmentation.
import Foundation
import Vision
import CoreImage
import AppKit

let args = CommandLine.arguments
let inURL = URL(fileURLWithPath: args[1])
let outURL = URL(fileURLWithPath: args[2])
guard let ci = CIImage(contentsOf: inURL) else { fatalError("cannot read input") }
let req = VNGeneratePersonSegmentationRequest()
req.qualityLevel = .accurate
req.outputPixelFormat = kCVPixelFormatType_OneComponent8
let handler = VNImageRequestHandler(ciImage: ci, options: [:])
try handler.perform([req])
guard let buf = req.results?.first?.pixelBuffer else { fatalError("no mask") }
var mask = CIImage(cvPixelBuffer: buf)
let sx = ci.extent.width / mask.extent.width, sy = ci.extent.height / mask.extent.height
mask = mask.transformed(by: CGAffineTransform(scaleX: sx, y: sy))
let ctx = CIContext()
let cs = CGColorSpaceCreateDeviceGray()
try ctx.writePNGRepresentation(of: mask, to: outURL, format: .L8, colorSpace: cs)
print("mask \(CVPixelBufferGetWidth(buf))x\(CVPixelBufferGetHeight(buf)) -> \(Int(ci.extent.width))x\(Int(ci.extent.height))")
